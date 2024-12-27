from . import XiaoduDeviceBase, XiaoduActions

class XiaoduAirPurifier(XiaoduDeviceBase):
    ''' 空气净化器 '''

    def __init__(self, entity_id) -> None:
        super().__init__(entity_id)
        self.device_type = 'AIR_PURIFIER'

    def device_info(self):
        return super().device_info(self.device_type, [
            XiaoduActions.turnOn,
            XiaoduActions.turnOff,
            XiaoduActions.getTurnOnState,
            XiaoduActions.setMode,
            XiaoduActions.getFanSpeed,
            XiaoduActions.setFanSpeed
        ], self.get_attribute())

    def get_attribute(self, default_value=None):
        return super().get_attribute([
            self.get_attribute_turnOnState(default_value),
            self.get_attribute_temperature(),
        ])

    def TurnOn(self, params):
        super().TurnOn(params)
        return {
            'attributes': self.get_attribute('ON')
        }

    def TurnOff(self, params):
        super().TurnOff(params)
        return {
            'attributes': self.get_attribute('OFF')
        }

    def SetMode(self, mode):
        super().SetMode(mode)
        return {
            'attributes': self.get_attribute()
        }

    def IncrementFanSpeed(self, deltaValue):
        super().IncrementFanSpeed(deltaValue)
        return {
            'attributes': self.get_attribute()
        }

    def DecrementFanSpeed(self, deltaValue):
        super().DecrementFanSpeed(deltaValue)
        return {
            'attributes': self.get_attribute()
        }
    
    def SetFanSpeed(self, params):
        super().SetFanSpeed(params)
        return {
            'attributes': self.get_attribute()
        }