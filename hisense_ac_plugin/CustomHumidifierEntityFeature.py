from homeassistant.components.humidifier import HumidifierEntityFeature

class CustomHumidifierEntityFeature(HumidifierEntityFeature):
    PRESET_MODES = 1 << 5  # 自定义预设模式支持
