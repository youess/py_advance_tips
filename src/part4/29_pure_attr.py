# -*- coding: utf-8 -*-


class Resistor(object):

    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0


# 直接使用公有属性
r1 = Resistor(50e3)
r1.ohms = 1e3
r1.ohms += 5e3


# 实现特殊行为
class VoltageResistance(Resistor):

    def __init__(self, ohms):
        super().__init__(ohms)
        self._voltage = 0

    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        self._voltage = voltage
        self.current = self._voltage / self.ohms


r2 = VoltageResistance(1e3)
print(f"Before: {r2.current} amps")
r2.voltage = 10
print(f"After: {r2.current} amps")


# 为属性setter指定类型和数值验证
class BoundedResistance(Resistor):

    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms     # how? Resistor没有这个属性，在setter里面进行调用

    @ohms.setter
    def ohms(self, ohms):
        if ohms <= 0:
            raise ValueError(f'{ohms} ohms must be > 0.')
        self._ohms = ohms


r3 = BoundedResistance(1e3)
print(f'r3.ohms = {r3.ohms}')
# r3.ohms = -1   # error
# BoundedResistance(0)   # also get error


# Fixed防止父类修改属性
class FixedResistance(Resistor):

    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if hasattr(self, '_ohms'):
            raise AttributeError("Can't set attribute")
        self._ohms = ohms


r4 = FixedResistance(1e3)
# r4.ohms = 2e3   # can't set
