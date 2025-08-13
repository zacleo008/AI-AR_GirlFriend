#!/usr/bin/env python3
"""
Integration Test for AI AR Girlfriend Application
Tests all system components working together
"""

import os
import sys
import json
import time
import requests
import subprocess
from datetime import datetime
from typing import Dict, Any, List

# 添加項目模組到路徑
sys.path.append('/home/ubuntu/ai_ar_girlfriend_app')

try:
    from emotion_engine import EmotionEngine
    from memory_system import MemorySystem
    from speech_system import SpeechSystem
    # Import the generator and renderer classes directly
    exec(open('/home/ubuntu/ai_ar_girlfriend_app/3d_model_generator.py').read())
    exec(open('/home/ubuntu/ai_ar_girlfriend_app/ar_renderer.py').read())
except ImportError as e:
    print(f"Import error: {e}")
    print("Some modules may not be available, continuing with available components...")

class IntegrationTester:
    """整合測試器"""
    
    def __init__(self):
        self.test_results = []
        self.backend_url = "http://localhost:5002"
        self.frontend_url = "http://localhost:5173"
        
        # 初始化系統組件
        self.emotion_engine = EmotionEngine()
        self.memory_system = MemorySystem()
        self.speech_system = SpeechSystem()
        self.model_generator = Model3DGenerator()
        self.ar_renderer = ARRenderer()
        
        self.test_user_id = "integration_test_user"
    
    def run_all_tests(self):
        """執行所有整合測試"""
        print("=== AI AR女友應用程式整合測試 ===")
        print(f"測試開始時間: {datetime.now().isoformat()}")
        
        # 測試各個組件
        self.test_emotion_engine()
        self.test_memory_system()
        self.test_speech_system()
        self.test_3d_model_system()
        self.test_ar_renderer()
        
        # 測試系統整合
        self.test_complete_conversation_flow()
        self.test_emotion_memory_integration()
        self.test_speech_emotion_integration()
        
        # 測試前後端整合
        self.test_backend_api()
        self.test_frontend_backend_integration()
        
        # 生成測試報告
        self.generate_test_report()
    
    def test_emotion_engine(self):
        """測試情感引擎"""
        print("\n🧠 測試情感引擎...")
        
        try:
            # 測試情感分析
            test_message = "我今天很開心，想和你聊天！"
            emotion_result = self.emotion_engine.analyze_emotion(test_message)
            
            assert emotion_result['primary_emotion'] in ['happiness', 'excitement', 'love']
            assert 0 <= emotion_result['intensity'] <= 1
            
            # 測試情感回應生成
            response = self.emotion_engine.generate_emotional_response(emotion_result, test_message)
            
            assert 'response_text' in response
            assert 'ai_emotion' in response
            assert 'animation' in response
            
            # 測試關係狀態更新
            self.emotion_engine.update_relationship_dynamics('positive_interaction', 
                                                           emotion_result['primary_emotion'], response)
            
            relationship_status = self.emotion_engine.get_relationship_status()
            assert relationship_status['intimacy_level'] >= 1.0
            
            self.add_test_result("情感引擎", True, "所有情感處理功能正常")
            
        except Exception as e:
            self.add_test_result("情感引擎", False, f"錯誤: {str(e)}")
    
    def test_memory_system(self):
        """測試記憶系統"""
        print("\n💾 測試記憶系統...")
        
        try:
            # 測試對話儲存
            conversation_id = self.memory_system.store_conversation(
                self.test_user_id,
                "我叫測試用戶，我喜歡看電影",
                "很高興認識你！我們可以聊聊電影。",
                {'primary_emotion': 'happiness', 'intensity': 0.8},
                'happiness'
            )
            
            assert conversation_id > 0
            
            # 測試對話歷史檢索
            history = self.memory_system.get_conversation_history(self.test_user_id, limit=10)
            assert len(history) > 0
            
            # 測試個人事實提取
            facts = self.memory_system.get_personal_facts(self.test_user_id)
            assert len(facts) > 0
            
            # 測試關係狀態更新
            self.memory_system.update_relationship_status(
                self.test_user_id,
                intimacy_level=2.0,
                trust_level=0.8,
                interaction_count=1
            )
            
            relationship = self.memory_system.get_relationship_status(self.test_user_id)
            assert relationship['intimacy_level'] == 2.0
            
            # 測試記憶搜索
            search_results = self.memory_system.search_memories(self.test_user_id, "電影")
            assert len(search_results) > 0
            
            self.add_test_result("記憶系統", True, "所有記憶功能正常")
            
        except Exception as e:
            self.add_test_result("記憶系統", False, f"錯誤: {str(e)}")
    
    def test_speech_system(self):
        """測試語音系統"""
        print("\n🎤 測試語音系統...")
        
        try:
            # 測試語音識別
            start_result = self.speech_system.start_speech_recognition(self.test_user_id)
            assert start_result['success'] == True
            
            time.sleep(1)  # 模擬錄音時間
            
            stop_result = self.speech_system.stop_speech_recognition()
            assert stop_result['success'] == True
            assert 'transcription' in stop_result
            
            # 測試文字轉語音
            tts_result = self.speech_system.text_to_speech(
                "你好，這是測試語音合成功能。",
                emotion="happiness"
            )
            assert tts_result['success'] == True
            assert 'audio_file' in tts_result
            
            # 測試語音命令處理
            command_result = self.speech_system.process_voice_command({
                'text': '停止播放',
                'confidence': 0.95
            })
            assert command_result['is_command'] == True
            assert command_result['command'] == 'stop'
            
            # 測試語音配置
            voice_profiles = self.speech_system.get_voice_profiles()
            assert len(voice_profiles) > 0
            
            self.add_test_result("語音系統", True, "所有語音功能正常")
            
        except Exception as e:
            self.add_test_result("語音系統", False, f"錯誤: {str(e)}")
    
    def test_3d_model_system(self):
        """測試3D模型系統"""
        print("\n🎨 測試3D模型系統...")
        
        try:
            # 測試模型生成
            model_data = self.model_generator.generate_from_text(
                prompt="可愛的動漫風格女孩",
                style="anime"
            )
            
            assert 'id' in model_data
            assert 'file_path' in model_data
            assert os.path.exists(model_data['file_path'])
            
            # 測試模型自定義
            customized_model = self.model_generator.customize_model(
                model_data['id'],
                {'hair_color': 'blue', 'eye_color': 'green'}
            )
            
            assert customized_model['hair_color'] == 'blue'
            assert customized_model['eye_color'] == 'green'
            
            # 測試可用模型列表
            available_models = self.model_generator.get_available_models()
            assert 'default_models' in available_models
            assert 'generated_models' in available_models
            
            # 測試動畫列表
            animations = self.model_generator.get_model_animations(model_data['id'])
            assert len(animations) > 0
            
            self.add_test_result("3D模型系統", True, "所有3D模型功能正常")
            
        except Exception as e:
            self.add_test_result("3D模型系統", False, f"錯誤: {str(e)}")
    
    def test_ar_renderer(self):
        """測試AR渲染器"""
        print("\n🥽 測試AR渲染器...")
        
        try:
            # 測試AR會話初始化
            ar_result = self.ar_renderer.initialize_ar_session()
            assert ar_result['success'] == True
            
            # 創建測試模型數據
            test_model = {
                'id': 'test_model',
                'name': '測試模型',
                'file_path': '/home/ubuntu/ai_ar_girlfriend_app/models/test.glb',
                'metadata': {'polygon_count': 10000}
            }
            
            # 創建模擬模型文件
            os.makedirs(os.path.dirname(test_model['file_path']), exist_ok=True)
            with open(test_model['file_path'], 'w') as f:
                f.write("# Test model file")
            
            # 測試模型載入
            load_result = self.ar_renderer.load_3d_model(test_model)
            assert load_result['success'] == True
            
            # 測試動畫播放
            anim_result = self.ar_renderer.play_animation('idle', loop=True)
            assert anim_result['success'] == True
            
            # 測試空間音頻
            audio_result = self.ar_renderer.play_spatial_audio({'text': '測試音頻'})
            assert audio_result['success'] == True
            
            # 測試渲染統計
            stats = self.ar_renderer.get_render_stats()
            assert 'ar_active' in stats
            assert 'model_loaded' in stats
            
            self.add_test_result("AR渲染器", True, "所有AR功能正常")
            
        except Exception as e:
            self.add_test_result("AR渲染器", False, f"錯誤: {str(e)}")
    
    def test_complete_conversation_flow(self):
        """測試完整對話流程"""
        print("\n💬 測試完整對話流程...")
        
        try:
            # 模擬完整的對話流程
            user_message = "我今天心情不太好"
            
            # 1. 情感分析
            emotion_result = self.emotion_engine.analyze_emotion(user_message)
            
            # 2. 生成情感回應
            ai_response = self.emotion_engine.generate_emotional_response(emotion_result, user_message)
            
            # 3. 儲存到記憶系統
            conversation_id = self.memory_system.store_conversation(
                self.test_user_id,
                user_message,
                ai_response['response_text'],
                emotion_result,
                ai_response['ai_emotion']
            )
            
            # 4. 更新關係狀態
            self.emotion_engine.update_relationship_dynamics(
                'positive_interaction',
                emotion_result['primary_emotion'],
                ai_response
            )
            
            # 5. 生成語音回應
            tts_result = self.speech_system.text_to_speech(
                ai_response['response_text'],
                ai_response['ai_emotion']
            )
            
            # 驗證流程完整性
            assert conversation_id > 0
            assert tts_result['success'] == True
            assert ai_response['ai_emotion'] in ['love', 'calmness']  # 對悲傷的適當回應
            
            self.add_test_result("完整對話流程", True, "對話流程整合正常")
            
        except Exception as e:
            self.add_test_result("完整對話流程", False, f"錯誤: {str(e)}")
    
    def test_emotion_memory_integration(self):
        """測試情感與記憶整合"""
        print("\n🧠💾 測試情感與記憶整合...")
        
        try:
            # 儲存情感記憶
            self.memory_system.store_emotional_memory(
                self.test_user_id,
                'happiness',
                0.8,
                '用戶分享開心事情',
                'celebrate',
                0.9
            )
            
            # 獲取情感模式
            emotion_patterns = self.memory_system.get_emotional_patterns(self.test_user_id)
            assert 'emotion_statistics' in emotion_patterns
            
            # 獲取情感洞察
            insights = self.emotion_engine.get_emotional_insights()
            assert 'most_common_user_emotion' in insights
            
            self.add_test_result("情感記憶整合", True, "情感與記憶整合正常")
            
        except Exception as e:
            self.add_test_result("情感記憶整合", False, f"錯誤: {str(e)}")
    
    def test_speech_emotion_integration(self):
        """測試語音與情感整合"""
        print("\n🎤🧠 測試語音與情感整合...")
        
        try:
            # 模擬語音識別結果
            speech_result = {
                'text': '我很興奮！',
                'confidence': 0.95,
                'emotion_analysis': {
                    'primary_emotion': 'excitement',
                    'intensity': 0.8
                }
            }
            
            # 處理語音情感
            text_emotion = self.emotion_engine.analyze_emotion(speech_result['text'])
            
            # 生成情感回應
            response = self.emotion_engine.generate_emotional_response(text_emotion, speech_result['text'])
            
            # 生成語音回應
            tts_result = self.speech_system.text_to_speech(
                response['response_text'],
                response['ai_emotion']
            )
            
            assert tts_result['success'] == True
            assert response['ai_emotion'] in ['excitement', 'happiness']
            
            self.add_test_result("語音情感整合", True, "語音與情感整合正常")
            
        except Exception as e:
            self.add_test_result("語音情感整合", False, f"錯誤: {str(e)}")
    
    def test_backend_api(self):
        """測試後端API"""
        print("\n🔗 測試後端API...")
        
        try:
            # 檢查後端服務是否運行
            try:
                response = requests.get(f"{self.backend_url}/api/users", timeout=5)
                backend_running = True
            except:
                backend_running = False
            
            if not backend_running:
                self.add_test_result("後端API", False, "後端服務未運行")
                return
            
            # 測試對話API
            conversation_data = {
                'user_id': self.test_user_id,
                'message': '測試API對話',
                'emotion': 'happiness'
            }
            
            try:
                response = requests.post(
                    f"{self.backend_url}/api/conversation",
                    json=conversation_data,
                    timeout=10
                )
                api_working = response.status_code == 200
            except:
                api_working = False
            
            if api_working:
                self.add_test_result("後端API", True, "API端點正常響應")
            else:
                self.add_test_result("後端API", False, "API端點無響應或錯誤")
                
        except Exception as e:
            self.add_test_result("後端API", False, f"錯誤: {str(e)}")
    
    def test_frontend_backend_integration(self):
        """測試前後端整合"""
        print("\n🌐 測試前後端整合...")
        
        try:
            # 檢查前端服務是否運行
            try:
                response = requests.get(self.frontend_url, timeout=5)
                frontend_running = response.status_code == 200
            except:
                frontend_running = False
            
            if frontend_running:
                self.add_test_result("前後端整合", True, "前端服務正常運行")
            else:
                self.add_test_result("前後端整合", False, "前端服務未運行")
                
        except Exception as e:
            self.add_test_result("前後端整合", False, f"錯誤: {str(e)}")
    
    def add_test_result(self, test_name: str, success: bool, message: str):
        """添加測試結果"""
        result = {
            'test_name': test_name,
            'success': success,
            'message': message,
            'timestamp': datetime.now().isoformat()
        }
        self.test_results.append(result)
        
        status = "✅ 通過" if success else "❌ 失敗"
        print(f"   {status}: {test_name} - {message}")
    
    def generate_test_report(self):
        """生成測試報告"""
        print("\n📊 生成測試報告...")
        
        total_tests = len(self.test_results)
        passed_tests = sum(1 for result in self.test_results if result['success'])
        failed_tests = total_tests - passed_tests
        
        success_rate = (passed_tests / total_tests) * 100 if total_tests > 0 else 0
        
        report = {
            'test_summary': {
                'total_tests': total_tests,
                'passed_tests': passed_tests,
                'failed_tests': failed_tests,
                'success_rate': round(success_rate, 2)
            },
            'test_results': self.test_results,
            'generated_at': datetime.now().isoformat(),
            'overall_status': 'PASS' if failed_tests == 0 else 'FAIL'
        }
        
        # 儲存報告
        report_path = "/home/ubuntu/ai_ar_girlfriend_app/integration_test_report.json"
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        
        # 顯示摘要