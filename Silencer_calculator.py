import iapws
from iapws import IAPWS97

"""
THIS IS THE MAIN BODY OF THE PROGRAMME
"""


def get_inputs():
      print("---- SILENCER SIZE CALCULATOR -----\n")

      # steam_up_pres = (float(input("UPSTREAM STEAM PRESSURE(barA):  ")))
      # steam_up_temp = float(input("UPSTREAM STEAM TEMPERATURE(°C):  "))
      # steam_flow_mass = float(input("STEAM FLOWRATE(kg/h):  "))
      # p_atm = float(input("ATMOSPHERIC PRESSURE(barA):  "))
      # # run this later

      steam_up_pres = 7
      steam_up_temp = 165
      steam_flow_mass = 5000
      p_atm = 0
      # diff_pres = float(input("DESIRED DIFFUSER PRESSURE(barA):  "))

      steam_cond = IAPWS97(P=steam_up_pres / 10, T=steam_up_temp + 273.15)
      hs1 = steam_cond.h
      vs_atm = iapws.iapws97._Backward3a_v_Ph(p_atm / 10, hs1)
      steam_flow_vol = vs_atm / steam_flow_mass * 3600

      print("\nUpstream Steam Properties:\nPressure: ", steam_up_pres, " barA \nTemperature: ", steam_up_temp,
            " °C \nEnthalpy: ",
            steam_cond.h, "kJ/kg \nSpecific Volume: ", vs_atm, "m3/kg \nVolumetric Flow Rate through Silencer: ",
            steam_flow_vol, "m3/s")


class Calculator:
    def __init__(self):
        pass


