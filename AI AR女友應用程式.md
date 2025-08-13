# AI AR女友應用程式

一個結合人工智能、擴增實境、3D模型生成和情感智能的虛擬伴侶應用程式。

## 🌟 專案特色

- 🧠 **智能情感交互**: 基於情感分析的個性化回應
- 🥽 **沉浸式AR體驗**: 真實環境中的虛擬角色互動
- 🎨 **3D角色生成**: 文字描述自動生成3D模型
- 🎤 **語音交互**: 語音識別和情感化語音合成
- 💾 **長期記憶**: 智能對話記憶和關係發展追蹤
- 🎭 **個性化**: 基於五大人格特質的AI個性系統

## 🚀 快速開始

### 系統要求

- Ubuntu 22.04 或相容系統
- Python 3.11+
- Node.js 20.18.0+
- 支援WebGL的現代瀏覽器

### 安裝步驟

1. **克隆專案**
```bash
git clone <repository-url>
cd ai_ar_girlfriend_app
```

2. **設置後端環境**
```bash
cd ai_backend
python3.11 -m venv venv
source venv/bin/activate
pip install flask flask-cors requests
```

3. **設置前端環境**
```bash
cd ../ar_frontend
npm install
```

4. **啟動應用**

後端服務:
```bash
cd ai_backend
source venv/bin/activate
python src/main.py
```

前端服務:
```bash
cd ar_frontend
npm run dev
```

5. **訪問應用**
- 前端: http://localhost:5173
- 後端API: http://localhost:5002

## 📱 使用說明

### 基本功能

1. **開始對話**
   - 點擊「開始對話」按鈕
   - 輸入文字訊息或使用語音輸入
   - AI女友會根據情感狀態回應

2. **AR互動**
   - 切換到「AR互動」標籤
   - 觀看3D角色動畫
   - 體驗空間音頻效果

3. **角色自定義**
   - 切換到「自定義」標籤
   - 選擇預設提示詞或輸入自定義描述
   - 點擊「生成3D模型」創建角色

### 進階功能

- **情感追蹤**: 系統會記錄和分析對話中的情感
- **關係發展**: 長期互動會影響親密度和信任度
- **個人記憶**: AI會記住用戶的個人信息和偏好
- **語音命令**: 支援「停止」、「暫停」等語音控制

## 🏗️ 系統架構

### 前端 (React)
```
ar_frontend/
├── src/
│   ├── App.jsx                 # 主應用組件
│   ├── components/
│   │   ├── ARViewer.jsx        # AR顯示組件
│   │   ├── ChatInterface.jsx   # 聊天介面
│   │   └── ModelCustomizer.jsx # 模型自定義
│   └── hooks/
│       └── useAIGirlfriend.js  # AI女友邏輯
```

### 後端 (Flask)
```
ai_backend/
├── src/
│   ├── main.py                 # Flask主程式
│   └── routes/
│       ├── ai_core.py          # AI核心API
│       ├── speech_service.py   # 語音服務API
│       ├── model_3d.py         # 3D模型API
│       └── user.py             # 用戶管理API
```

### 核心系統
```
├── emotion_engine.py           # 情感智能引擎
├── memory_system.py            # 長期記憶系統
├── speech_system.py            # 語音交互系統
├── 3d_model_generator.py       # 3D模型生成器
└── ar_renderer.py              # AR渲染引擎
```

## 🧪 測試

### 運行整合測試
```bash
python integration_test.py
```

### 測試覆蓋範圍
- ✅ 情感引擎功能測試
- ✅ 記憶系統功能測試
- ✅ 語音系統功能測試
- ✅ 3D模型系統測試
- ✅ AR渲染器測試
- ✅ 完整對話流程測試
- ✅ 系統整合測試

## 📊 API文檔

### 對話API
```http
POST /api/conversation
Content-Type: application/json

{
  "user_id": "string",
  "message": "string",
  "emotion": "string"
}
```

### 3D模型生成API
```http
POST /api/models/generate
Content-Type: application/json

{
  "user_id": "string",
  "prompt": "string",
  "style": "anime|realistic",
  "customization": {}
}
```

### 語音服務API
```http
POST /api/speech/recognize
POST /api/speech/synthesize
```

## 🔧 配置選項

### 情感引擎配置
```python
emotion_states = {
    'happiness': 0.5,
    'sadness': 0.1,
    'love': 0.3,
    # ...
}
```

### 語音系統配置
```python
speech_config = {
    'sample_rate': 16000,
    'max_recording_duration': 30,
    'voice_type': 'female'
}
```

### 記憶系統配置
```python
memory_config = {
    'max_conversation_history': 1000,
    'memory_decay_days': 30,
    'importance_threshold': 0.5
}
```

## 🐛 故障排除

### 常見問題

1. **後端服務無法啟動**
   - 檢查Python虛擬環境是否正確激活
   - 確認所有依賴已安裝
   - 檢查端口5002是否被占用

2. **前端無法連接後端**
   - 確認後端服務正在運行
   - 檢查CORS配置
   - 驗證API端點URL

3. **3D模型無法顯示**
   - 檢查瀏覽器WebGL支援
   - 確認模型文件路徑正確
   - 檢查AR渲染器初始化

### 日誌查看
```bash
# 後端日誌
tail -f ai_backend/server.log

# 前端開發日誌
npm run dev --verbose
```

## 🤝 貢獻指南

### 開發流程
1. Fork專案
2. 創建功能分支
3. 提交更改
4. 運行測試
5. 提交Pull Request

### 代碼規範
- Python: 遵循PEP 8
- JavaScript: 使用ESLint配置
- 組件: 使用函數式組件和Hooks
- API: RESTful設計原則

## 📄 授權

本專案採用MIT授權條款。詳見 [LICENSE](LICENSE) 文件。

## 🙏 致謝

- OpenAI - AI技術支援
- React團隊 - 前端框架
- Flask團隊 - 後端框架
- 開源社區 - 各種優秀工具和庫

## 📞 聯繫方式

- 專案負責人: Manus AI Agent
- 技術支援: Manus Team
- 問題回報: 請使用GitHub Issues

---

**版本**: 1.0.0  
**最後更新**: 2025年8月13日  
**狀態**: ✅ 生產就緒

