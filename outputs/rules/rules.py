def findDecision(obj): #obj[0]: C_600570, obj[1]: C_660570, obj[2]: C_500300, obj[3]: C_500600, obj[4]: C_501200, obj[5]: C_502400, obj[6]: C_111620, obj[7]: C_111640, obj[8]: C_111660, obj[9]: C_106860, obj[10]: C_106880, obj[11]: C_106920, obj[12]: C_100100, obj[13]: C_100110, obj[14]: C_100120, obj[15]: C_100140, obj[16]: C_100160, obj[17]: C_104320, obj[18]: C_100000, obj[19]: C_750100, obj[20]: C_750300, obj[21]: C_750600, obj[22]: C_751200, obj[23]: C_752400, obj[24]: C_111500, obj[25]: C_650640, obj[26]: C_906170, obj[27]: C_930623, obj[28]: C_102800, obj[29]: C_106800, obj[30]: C_106820, obj[31]: C_107480, obj[32]: C_110720, obj[33]: C_906370, obj[34]: C_912070, obj[35]: C_999032, obj[36]: C_103380, obj[37]: C_106600, obj[38]: C_111300, obj[39]: C_111780, obj[40]: C_990370, obj[41]: C_114100, obj[42]: C_600160, obj[43]: C_961223, obj[44]: C_105740, obj[45]: C_116000, obj[46]: C_990660, obj[47]: C_100900, obj[48]: C_111600, obj[49]: C_114900
   # {"feature": "C_600570", "instances": 320180, "metric_value": 3342.7418, "depth": 1}
   if obj[0] == '10000':
      # {"feature": "C_660570", "instances": 64468, "metric_value": 629.6872, "depth": 2}
      if obj[1] == '10000':
         # {"feature": "C_906370", "instances": 52147, "metric_value": 389.5448, "depth": 3}
         if obj[33]>4.643277657391605:
            # {"feature": "C_104320", "instances": 27289, "metric_value": 272.6369, "depth": 4}
            if obj[17]>38.79903990618931:
               # {"feature": "C_106600", "instances": 13695, "metric_value": 193.1093, "depth": 5}
               if obj[37]>1.0:
                  return 'G'
               elif obj[37]<=1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[17]<=38.79903990618931:
               # {"feature": "C_106880", "instances": 13594, "metric_value": 192.5123, "depth": 5}
               if obj[10]>0.0:
                  return 'G'
               elif obj[10]<=0.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[33]<=4.643277657391605:
            # {"feature": "C_751200", "instances": 24858, "metric_value": 278.1362, "depth": 4}
            if obj[22]>1.0:
               # {"feature": "C_104320", "instances": 13845, "metric_value": 203.8607, "depth": 5}
               if obj[17]<=45.701047309498016:
                  return 'G'
               elif obj[17]>45.701047309498016:
                  return 'G'
               else:
                  return 'G'
            elif obj[22]<=1.0:
               # {"feature": "C_111500", "instances": 11013, "metric_value": 189.7661, "depth": 5}
               if obj[24]>-1.0:
                  return 'G'
               elif obj[24]<=-1.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '10011':
         # {"feature": "C_906370", "instances": 6663, "metric_value": 138.106, "depth": 3}
         if obj[33]>4.957226474561009:
            # {"feature": "C_116000", "instances": 3684, "metric_value": 101.0496, "depth": 4}
            if obj[45]>1.0:
               # {"feature": "C_103380", "instances": 1858, "metric_value": 68.1756, "depth": 5}
               if obj[36]<=19.293116254036597:
                  return 'G'
               elif obj[36]>19.293116254036597:
                  return 'G'
               else:
                  return 'G'
            elif obj[45]<=1.0:
               # {"feature": "C_502400", "instances": 1826, "metric_value": 74.9089, "depth": 5}
               if obj[5] == 'G':
                  return 'G'
               elif obj[5] == 'B':
                  return 'G'
               elif obj[5] == 'I':
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[33]<=4.957226474561009:
            # {"feature": "C_103380", "instances": 2979, "metric_value": 94.2478, "depth": 4}
            if obj[36]>32.58913058073178:
               # {"feature": "C_106600", "instances": 1582, "metric_value": 68.5649, "depth": 5}
               if obj[37]<=0.0:
                  return 'G'
               elif obj[37]>0.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[36]<=32.58913058073178:
               # {"feature": "C_502400", "instances": 1397, "metric_value": 65.1513, "depth": 5}
               if obj[5] == 'G':
                  return 'G'
               elif obj[5] == 'B':
                  return 'G'
               elif obj[5] == 'I':
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '10100':
         # {"feature": "C_906370", "instances": 1955, "metric_value": 77.3674, "depth": 3}
         if obj[33]>5.698209718670077:
            # {"feature": "C_116000", "instances": 1074, "metric_value": 57.7206, "depth": 4}
            if obj[45]>1.0:
               # {"feature": "C_106880", "instances": 612, "metric_value": 42.3517, "depth": 5}
               if obj[10]<=2.0:
                  return 'G'
               elif obj[10]>2.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[45]<=1.0:
               # {"feature": "C_502400", "instances": 462, "metric_value": 39.342, "depth": 5}
               if obj[5] == 'G':
                  return 'G'
               elif obj[5] == 'B':
                  return 'G'
               elif obj[5] == 'I':
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[33]<=5.698209718670077:
            # {"feature": "C_100120", "instances": 881, "metric_value": 51.8181, "depth": 4}
            if obj[14]>2.0:
               # {"feature": "C_106880", "instances": 490, "metric_value": 35.928, "depth": 5}
               if obj[10]<=2.0:
                  return 'G'
               elif obj[10]>2.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[14]<=2.0:
               # {"feature": "C_114100", "instances": 391, "metric_value": 37.3328, "depth": 5}
               if obj[41]>0.5227324808184143:
                  return 'G'
               elif obj[41]<=0.5227324808184143:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '10010':
         # {"feature": "C_502400", "instances": 1865, "metric_value": 79.0901, "depth": 3}
         if obj[5] == 'G':
            # {"feature": "C_906370", "instances": 1126, "metric_value": 64.1317, "depth": 4}
            if obj[33]>5.031083481349911:
               # {"feature": "C_116000", "instances": 563, "metric_value": 44.919, "depth": 5}
               if obj[45]<=1.0:
                  return 'G'
               elif obj[45]>1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[33]<=5.031083481349911:
               # {"feature": "C_103380", "instances": 563, "metric_value": 45.7729, "depth": 5}
               if obj[36]<=29.107655417406743:
                  return 'G'
               elif obj[36]>29.107655417406743:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[5] == 'B':
            # {"feature": "C_501200", "instances": 630, "metric_value": 38.8182, "depth": 4}
            if obj[4] == 'B':
               # {"feature": "C_500300", "instances": 336, "metric_value": 26.9612, "depth": 5}
               if obj[2] == 'G':
                  return 'G'
               elif obj[2] == 'B':
                  return 'G'
               elif obj[2] == 'I':
                  return 'B'
               else:
                  return 'G'
            elif obj[4] == 'G':
               # {"feature": "C_107480", "instances": 257, "metric_value": 27.9382, "depth": 5}
               if obj[31]<=44.872373540856024:
                  return 'G'
               elif obj[31]>44.872373540856024:
                  return 'G'
               else:
                  return 'G'
            elif obj[4] == 'I':
               # {"feature": "C_750100", "instances": 30, "metric_value": 10.0302, "depth": 5}
               if obj[19]<=2.0:
                  return 'G'
               elif obj[19]>2.0:
                  return 'B'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[5] == 'I':
            # {"feature": "C_750100", "instances": 103, "metric_value": 13.7619, "depth": 4}
            if obj[19]<=2.0:
               # {"feature": "C_104320", "instances": 86, "metric_value": 15.2444, "depth": 5}
               if obj[17]<=95.15116279069767:
                  return 'G'
               elif obj[17]>95.15116279069767:
                  return 'G'
               else:
                  return 'G'
            elif obj[19]>2.0:
               # {"feature": "C_104320", "instances": 17, "metric_value": 6.0166, "depth": 5}
               if obj[17]<=183.0:
                  return 'B'
               elif obj[17]>183.0:
                  return 'G'
               else:
                  return 'B'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '10111':
         # {"feature": "C_502400", "instances": 652, "metric_value": 45.2621, "depth": 3}
         if obj[5] == 'G':
            # {"feature": "C_107480", "instances": 468, "metric_value": 40.1748, "depth": 4}
            if obj[31]<=39.643803418803415:
               # {"feature": "C_116000", "instances": 293, "metric_value": 31.0123, "depth": 5}
               if obj[45]>1.0:
                  return 'G'
               elif obj[45]<=1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[31]>39.643803418803415:
               # {"feature": "C_906370", "instances": 175, "metric_value": 25.8528, "depth": 5}
               if obj[33]<=5.0:
                  return 'G'
               elif obj[33]>5.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[5] == 'B':
            # {"feature": "C_501200", "instances": 129, "metric_value": 18.1212, "depth": 4}
            if obj[4] == 'B':
               # {"feature": "C_111660", "instances": 81, "metric_value": 9.3515, "depth": 5}
               if obj[8]>0.0:
                  return 'G'
               elif obj[8]<=0.0:
                  return 'B'
               else:
                  return 'G'
            elif obj[4] == 'G':
               # {"feature": "C_106860", "instances": 39, "metric_value": 11.8635, "depth": 5}
               if obj[9]<=1.0:
                  return 'G'
               elif obj[9]>1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[4] == 'I':
               return 'G'
            else:
               return 'G'
         elif obj[5] == 'I':
            # {"feature": "C_750100", "instances": 55, "metric_value": 10.5516, "depth": 4}
            if obj[19]<=3.0:
               # {"feature": "C_104320", "instances": 51, "metric_value": 11.1698, "depth": 5}
               if obj[17]<=84.27450980392157:
                  return 'G'
               elif obj[17]>84.27450980392157:
                  return 'G'
               else:
                  return 'G'
            elif obj[19]>3.0:
               return 'B'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '11000':
         # {"feature": "C_502400", "instances": 483, "metric_value": 43.4363, "depth": 3}
         if obj[5] == 'G':
            # {"feature": "C_100120", "instances": 378, "metric_value": 35.801, "depth": 4}
            if obj[14]>3.0:
               # {"feature": "C_100000", "instances": 191, "metric_value": 25.059, "depth": 5}
               if obj[18]<=7.0:
                  return 'G'
               elif obj[18]>7.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[14]<=3.0:
               # {"feature": "C_906370", "instances": 187, "metric_value": 25.6293, "depth": 5}
               if obj[33]<=4.0:
                  return 'G'
               elif obj[33]>4.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[5] == 'B':
            # {"feature": "C_501200", "instances": 83, "metric_value": 17.3984, "depth": 4}
            if obj[4] == 'B':
               # {"feature": "C_500600", "instances": 43, "metric_value": 12.4028, "depth": 5}
               if obj[3] == 'B':
                  return 'G'
               elif obj[3] == 'G':
                  return 'G'
               elif obj[3] == 'I':
                  return 'G'
               else:
                  return 'G'
            elif obj[4] == 'G':
               return 'G'
            elif obj[4] == 'I':
               # {"feature": "C_106880", "instances": 3, "metric_value": 3.4142, "depth": 5}
               if obj[10]>2.0:
                  return 'G'
               elif obj[10]<=2.0:
                  return 'B'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[5] == 'I':
            return 'G'
         else:
            return 'G'
      elif obj[1] == '10110':
         # {"feature": "C_502400", "instances": 216, "metric_value": 26.97, "depth": 3}
         if obj[5] == 'G':
            # {"feature": "C_103380", "instances": 133, "metric_value": 22.7207, "depth": 4}
            if obj[36]<=14.29:
               # {"feature": "C_650640", "instances": 68, "metric_value": 16.0139, "depth": 5}
               if obj[25]>1900.0:
                  return 'G'
               elif obj[25]<=1900.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[36]>14.29:
               return 'G'
            else:
               return 'G'
         elif obj[5] == 'B':
            # {"feature": "C_111600", "instances": 74, "metric_value": 14.4447, "depth": 4}
            if obj[48]<=1.0:
               # {"feature": "C_500600", "instances": 66, "metric_value": 16.7633, "depth": 5}
               if obj[3] == 'G':
                  return 'G'
               elif obj[3] == 'B':
                  return 'G'
               elif obj[3] == 'I':
                  return 'G'
               else:
                  return 'G'
            elif obj[48]>1.0:
               return 'B'
            else:
               return 'G'
         elif obj[5] == 'I':
            # {"feature": "C_114100", "instances": 9, "metric_value": 5.7417, "depth": 4}
            if obj[41]<=0.7489:
               return 'G'
            elif obj[41]>0.7489:
               return 'B'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '10001':
         # {"feature": "C_906370", "instances": 167, "metric_value": 22.546, "depth": 3}
         if obj[33]>4.0:
            # {"feature": "C_111640", "instances": 94, "metric_value": 16.0228, "depth": 4}
            if obj[7]<=1.0:
               # {"feature": "C_100120", "instances": 87, "metric_value": 17.3763, "depth": 5}
               if obj[14]<=5.0:
                  return 'G'
               elif obj[14]>5.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[7]>1.0:
               return 'B'
            else:
               return 'G'
         elif obj[33]<=4.0:
            # {"feature": "C_100000", "instances": 73, "metric_value": 16.6226, "depth": 4}
            if obj[18]<=3.0:
               # {"feature": "C_114100", "instances": 37, "metric_value": 11.5231, "depth": 5}
               if obj[41]<=0.46893513513513513:
                  return 'G'
               elif obj[41]>0.46893513513513513:
                  return 'G'
               else:
                  return 'G'
            elif obj[18]>3.0:
               return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '11011':
         # {"feature": "C_502400", "instances": 110, "metric_value": 21.4811, "depth": 3}
         if obj[5] == 'G':
            # {"feature": "C_107480", "instances": 76, "metric_value": 16.9812, "depth": 4}
            if obj[31]<=80.02631578947368:
               # {"feature": "C_600160", "instances": 39, "metric_value": 11.8635, "depth": 5}
               if obj[42]<=36.0:
                  return 'G'
               elif obj[42]>36.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[31]>80.02631578947368:
               return 'G'
            else:
               return 'G'
         elif obj[5] == 'B':
            # {"feature": "C_500600", "instances": 27, "metric_value": 11.0572, "depth": 4}
            if obj[3] == 'G':
               return 'G'
            elif obj[3] == 'B':
               return 'G'
            elif obj[3] == 'I':
               return 'B'
            else:
               return 'G'
         elif obj[5] == 'I':
            # {"feature": "C_501200", "instances": 7, "metric_value": 4.8783, "depth": 4}
            if obj[4] == 'I':
               return 'G'
            elif obj[4] == 'G':
               return 'B'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '11100':
         # {"feature": "C_501200", "instances": 77, "metric_value": 14.5738, "depth": 3}
         if obj[4] == 'G':
            # {"feature": "C_100000", "instances": 62, "metric_value": 13.7296, "depth": 4}
            if obj[18]<=6.0:
               # {"feature": "C_104320", "instances": 32, "metric_value": 9.2963, "depth": 5}
               if obj[17]>79.9781591354794:
                  return 'G'
               elif obj[17]<=79.9781591354794:
                  return 'G'
               else:
                  return 'G'
            elif obj[18]>6.0:
               # {"feature": "C_100120", "instances": 30, "metric_value": 10.244, "depth": 5}
               if obj[14]>7.0:
                  return 'G'
               elif obj[14]<=7.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[4] == 'B':
            return 'G'
         elif obj[4] == 'I':
            # {"feature": "C_104320", "instances": 5, "metric_value": 4.4495, "depth": 4}
            if obj[17]<=250.0:
               return 'G'
            elif obj[17]>250.0:
               return 'B'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '11010':
         # {"feature": "C_502400", "instances": 76, "metric_value": 17.8089, "depth": 3}
         if obj[5] == 'G':
            return 'G'
         elif obj[5] == 'B':
            # {"feature": "C_500300", "instances": 30, "metric_value": 10.3117, "depth": 4}
            if obj[2] == 'G':
               return 'G'
            elif obj[2] == 'I':
               return 'G'
            elif obj[2] == 'B':
               return 'B'
            else:
               return 'G'
         elif obj[5] == 'I':
            # {"feature": "C_500300", "instances": 4, "metric_value": 3.8637, "depth": 4}
            if obj[2] == 'G':
               return 'G'
            elif obj[2] == 'I':
               return 'B'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '10101':
         return 'G'
      elif obj[1] == '11110':
         # {"feature": "C_500300", "instances": 12, "metric_value": 6.1046, "depth": 3}
         if obj[2] == 'G':
            return 'G'
         elif obj[2] == 'B':
            return 'B'
         else:
            return 'G'
      elif obj[1] == '11111':
         return 'G'
      elif obj[1] == '11001':
         return 'G'
      elif obj[1] == '11101':
         return 'G'
      else:
         return 'G'
   elif obj[0] == '10011':
      # {"feature": "C_660570", "instances": 31342, "metric_value": 309.6425, "depth": 2}
      if obj[1] == '10011':
         # {"feature": "C_912070", "instances": 27420, "metric_value": 266.816, "depth": 3}
         if obj[34]>0.0:
            # {"feature": "C_116000", "instances": 17015, "metric_value": 192.5938, "depth": 4}
            if obj[45]>2.0:
               # {"feature": "C_107480", "instances": 10143, "metric_value": 137.9661, "depth": 5}
               if obj[31]<=40.29750566893424:
                  return 'G'
               elif obj[31]>40.29750566893424:
                  return 'G'
               else:
                  return 'G'
            elif obj[45]<=2.0:
               # {"feature": "C_906170", "instances": 6872, "metric_value": 135.76, "depth": 5}
               if obj[26]>1.0:
                  return 'G'
               elif obj[26]<=1.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[34]<=0.0:
            # {"feature": "C_114100", "instances": 10405, "metric_value": 185.5999, "depth": 4}
            if obj[41]>0.6050566458433446:
               # {"feature": "C_107480", "instances": 5834, "metric_value": 134.4571, "depth": 5}
               if obj[31]<=41.7007027768255:
                  return 'G'
               elif obj[31]>41.7007027768255:
                  return 'G'
               else:
                  return 'G'
            elif obj[41]<=0.6050566458433446:
               # {"feature": "C_752400", "instances": 4571, "metric_value": 127.844, "depth": 5}
               if obj[23]<=1.0:
                  return 'G'
               elif obj[23]>1.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '10111':
         # {"feature": "C_912070", "instances": 2735, "metric_value": 86.7732, "depth": 3}
         if obj[34]>0.0:
            # {"feature": "C_502400", "instances": 1536, "metric_value": 63.0328, "depth": 4}
            if obj[5] == 'G':
               # {"feature": "C_110720", "instances": 1113, "metric_value": 57.4049, "depth": 5}
               if obj[32]>0.0:
                  return 'G'
               elif obj[32]<=0.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[5] == 'I':
               # {"feature": "C_750100", "instances": 228, "metric_value": 20.4253, "depth": 5}
               if obj[19]<=2.0:
                  return 'G'
               elif obj[19]>2.0:
                  return 'B'
               else:
                  return 'G'
            elif obj[5] == 'B':
               # {"feature": "C_501200", "instances": 195, "metric_value": 17.1717, "depth": 5}
               if obj[4] == 'B':
                  return 'G'
               elif obj[4] == 'G':
                  return 'G'
               elif obj[4] == 'I':
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[34]<=0.0:
            # {"feature": "C_106880", "instances": 1199, "metric_value": 62.1486, "depth": 4}
            if obj[10]>2.0:
               # {"feature": "C_104320", "instances": 639, "metric_value": 43.4509, "depth": 5}
               if obj[17]<=123.8810641627543:
                  return 'G'
               elif obj[17]>123.8810641627543:
                  return 'G'
               else:
                  return 'G'
            elif obj[10]<=2.0:
               # {"feature": "C_600160", "instances": 560, "metric_value": 44.4453, "depth": 5}
               if obj[42]<=20.103571428571428:
                  return 'G'
               elif obj[42]>20.103571428571428:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '11011':
         # {"feature": "C_114100", "instances": 984, "metric_value": 59.2284, "depth": 3}
         if obj[41]>0.6024392276422764:
            # {"feature": "C_116000", "instances": 542, "metric_value": 42.1746, "depth": 4}
            if obj[45]>2.0:
               # {"feature": "C_600160", "instances": 297, "metric_value": 29.43, "depth": 5}
               if obj[42]>30.343434343434343:
                  return 'G'
               elif obj[42]<=30.343434343434343:
                  return 'G'
               else:
                  return 'G'
            elif obj[45]<=2.0:
               # {"feature": "C_502400", "instances": 245, "metric_value": 30.3032, "depth": 5}
               if obj[5] == 'G':
                  return 'G'
               elif obj[5] == 'B':
                  return 'G'
               elif obj[5] == 'I':
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[41]<=0.6024392276422764:
            # {"feature": "C_502400", "instances": 442, "metric_value": 41.8767, "depth": 4}
            if obj[5] == 'G':
               # {"feature": "C_104320", "instances": 391, "metric_value": 39.1252, "depth": 5}
               if obj[17]<=247.462915601023:
                  return 'G'
               elif obj[17]>247.462915601023:
                  return 'G'
               else:
                  return 'G'
            elif obj[5] == 'B':
               return 'G'
            elif obj[5] == 'I':
               return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '11111':
         # {"feature": "C_502400", "instances": 203, "metric_value": 27.5963, "depth": 3}
         if obj[5] == 'G':
            # {"feature": "C_104320", "instances": 168, "metric_value": 25.012, "depth": 4}
            if obj[17]<=234.2202380952381:
               # {"feature": "C_100120", "instances": 89, "metric_value": 17.6286, "depth": 5}
               if obj[14]>3.0:
                  return 'G'
               elif obj[14]<=3.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[17]>234.2202380952381:
               return 'G'
            else:
               return 'G'
         elif obj[5] == 'B':
            # {"feature": "C_500600", "instances": 21, "metric_value": 7.8425, "depth": 4}
            if obj[3] == 'G':
               # {"feature": "C_501200", "instances": 12, "metric_value": 5.5117, "depth": 5}
               if obj[4] == 'G':
                  return 'G'
               elif obj[4] == 'B':
                  return 'G'
               elif obj[4] == 'I':
                  return 'G'
               else:
                  return 'G'
            elif obj[3] == 'B':
               return 'G'
            elif obj[3] == 'I':
               # {"feature": "C_111660", "instances": 4, "metric_value": 3.8637, "depth": 5}
               if obj[8]>1.0:
                  return 'G'
               elif obj[8]<=1.0:
                  return 'B'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[5] == 'I':
            return 'G'
         else:
            return 'G'
      else:
         return 'G'
   elif obj[0] == '10010':
      # {"feature": "C_660570", "instances": 23845, "metric_value": 363.1932, "depth": 2}
      if obj[1] == '10010':
         # {"feature": "C_114100", "instances": 18587, "metric_value": 237.4431, "depth": 3}
         if obj[41]>0.6332356539516867:
            # {"feature": "C_999032", "instances": 10519, "metric_value": 169.7029, "depth": 4}
            if obj[35]>0.0:
               # {"feature": "C_107480", "instances": 6010, "metric_value": 120.3099, "depth": 5}
               if obj[31]<=29.120499168053243:
                  return 'G'
               elif obj[31]>29.120499168053243:
                  return 'G'
               else:
                  return 'G'
            elif obj[35]<=0.0:
               # {"feature": "C_600160", "instances": 4509, "metric_value": 120.1829, "depth": 5}
               if obj[42]<=19.000443557329785:
                  return 'G'
               elif obj[42]>19.000443557329785:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[41]<=0.6332356539516867:
            # {"feature": "C_600160", "instances": 8068, "metric_value": 166.4195, "depth": 4}
            if obj[42]<=17.750619732275656:
               # {"feature": "C_750600", "instances": 4298, "metric_value": 122.4571, "depth": 5}
               if obj[21]>1.0:
                  return 'G'
               elif obj[21]<=1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[42]>17.750619732275656:
               # {"feature": "C_650640", "instances": 3770, "metric_value": 112.928, "depth": 5}
               if obj[25]<=1775.9106100795757:
                  return 'G'
               elif obj[25]>1775.9106100795757:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '10011':
         # {"feature": "C_999032", "instances": 2682, "metric_value": 87.763, "depth": 3}
         if obj[35]>0.0:
            # {"feature": "C_107480", "instances": 1419, "metric_value": 60.7346, "depth": 4}
            if obj[31]<=40.28322762508809:
               # {"feature": "C_114100", "instances": 861, "metric_value": 44.4291, "depth": 5}
               if obj[41]>0.7194649245063879:
                  return 'G'
               elif obj[41]<=0.7194649245063879:
                  return 'G'
               else:
                  return 'G'
            elif obj[31]>40.28322762508809:
               # {"feature": "C_100000", "instances": 558, "metric_value": 41.6928, "depth": 5}
               if obj[18]>5.0:
                  return 'G'
               elif obj[18]<=5.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[35]<=0.0:
            # {"feature": "C_600160", "instances": 1263, "metric_value": 63.556, "depth": 4}
            if obj[42]>23.49643705463183:
               # {"feature": "C_103380", "instances": 690, "metric_value": 45.6657, "depth": 5}
               if obj[36]<=17.781536231884058:
                  return 'G'
               elif obj[36]>17.781536231884058:
                  return 'G'
               else:
                  return 'G'
            elif obj[42]<=23.49643705463183:
               # {"feature": "C_106880", "instances": 573, "metric_value": 44.2023, "depth": 5}
               if obj[10]>1.0:
                  return 'G'
               elif obj[10]<=1.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '10110':
         # {"feature": "C_999032", "instances": 1492, "metric_value": 70.0039, "depth": 3}
         if obj[35]>0.0:
            # {"feature": "C_106880", "instances": 746, "metric_value": 48.3448, "depth": 4}
            if obj[10]>2.0:
               # {"feature": "C_502400", "instances": 381, "metric_value": 33.5769, "depth": 5}
               if obj[5] == 'G':
                  return 'G'
               elif obj[5] == 'I':
                  return 'G'
               elif obj[5] == 'B':
                  return 'G'
               else:
                  return 'G'
            elif obj[10]<=2.0:
               # {"feature": "C_110720", "instances": 365, "metric_value": 35.0889, "depth": 5}
               if obj[32]<=6.838356164383562:
                  return 'G'
               elif obj[32]>6.838356164383562:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[35]<=0.0:
            # {"feature": "C_600160", "instances": 746, "metric_value": 50.6581, "depth": 4}
            if obj[42]>24.2828418230563:
               # {"feature": "C_110720", "instances": 409, "metric_value": 36.9049, "depth": 5}
               if obj[32]<=8.777506112469437:
                  return 'G'
               elif obj[32]>8.777506112469437:
                  return 'G'
               else:
                  return 'G'
            elif obj[42]<=24.2828418230563:
               # {"feature": "C_100000", "instances": 337, "metric_value": 34.754, "depth": 5}
               if obj[18]<=4.0:
                  return 'G'
               elif obj[18]>4.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '11010':
         # {"feature": "C_502400", "instances": 448, "metric_value": 41.7836, "depth": 3}
         if obj[5] == 'G':
            # {"feature": "C_104320", "instances": 390, "metric_value": 38.2711, "depth": 4}
            if obj[17]<=232.69230769230768:
               # {"feature": "C_100120", "instances": 208, "metric_value": 27.7187, "depth": 5}
               if obj[14]<=3.0:
                  return 'G'
               elif obj[14]>3.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[17]>232.69230769230768:
               # {"feature": "C_110720", "instances": 182, "metric_value": 26.3867, "depth": 5}
               if obj[32]<=7.857142857142857:
                  return 'G'
               elif obj[32]>7.857142857142857:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[5] == 'B':
            # {"feature": "C_501200", "instances": 31, "metric_value": 12.4345, "depth": 4}
            if obj[4] == 'G':
               return 'G'
            elif obj[4] == 'B':
               # {"feature": "C_500600", "instances": 13, "metric_value": 8.3181, "depth": 5}
               if obj[3] == 'B':
                  return 'G'
               elif obj[3] == 'G':
                  return 'G'
               elif obj[3] == 'I':
                  return 'B'
               else:
                  return 'G'
            elif obj[4] == 'I':
               return 'G'
            else:
               return 'G'
         elif obj[5] == 'I':
            return 'G'
         else:
            return 'G'
      elif obj[1] == '10111':
         # {"feature": "C_110720", "instances": 443, "metric_value": 34.5103, "depth": 3}
         if obj[32]<=7.36117381489842:
            # {"feature": "C_114100", "instances": 249, "metric_value": 25.0967, "depth": 4}
            if obj[41]>0.7217843373493976:
               # {"feature": "C_502400", "instances": 154, "metric_value": 19.6473, "depth": 5}
               if obj[5] == 'G':
                  return 'G'
               elif obj[5] == 'I':
                  return 'B'
               elif obj[5] == 'B':
                  return 'G'
               else:
                  return 'G'
            elif obj[41]<=0.7217843373493976:
               # {"feature": "C_502400", "instances": 95, "metric_value": 17.5176, "depth": 5}
               if obj[5] == 'G':
                  return 'G'
               elif obj[5] == 'I':
                  return 'G'
               elif obj[5] == 'B':
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[32]>7.36117381489842:
            # {"feature": "C_100000", "instances": 194, "metric_value": 23.8702, "depth": 4}
            if obj[18]>7.0:
               # {"feature": "C_106880", "instances": 108, "metric_value": 16.9834, "depth": 5}
               if obj[10]>3.0:
                  return 'G'
               elif obj[10]<=3.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[18]<=7.0:
               # {"feature": "C_502400", "instances": 86, "metric_value": 16.8943, "depth": 5}
               if obj[5] == 'G':
                  return 'G'
               elif obj[5] == 'B':
                  return 'G'
               elif obj[5] == 'I':
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '11011':
         # {"feature": "C_100140", "instances": 96, "metric_value": 17.614, "depth": 3}
         if obj[15]<=2.0:
            # {"feature": "C_110720", "instances": 60, "metric_value": 13.0479, "depth": 4}
            if obj[32]>2.0:
               # {"feature": "C_116000", "instances": 39, "metric_value": 9.6585, "depth": 5}
               if obj[45]<=4.0:
                  return 'G'
               elif obj[45]>4.0:
                  return 'B'
               else:
                  return 'G'
            elif obj[32]<=2.0:
               return 'G'
            else:
               return 'G'
         elif obj[15]>2.0:
            return 'G'
         else:
            return 'G'
      elif obj[1] == '11110':
         return 'G'
      elif obj[1] == '11111':
         return 'G'
      else:
         return 'G'
   elif obj[0] == '11011':
      # {"feature": "C_912070", "instances": 21552, "metric_value": 265.6853, "depth": 2}
      if obj[34]>0.0:
         # {"feature": "C_116000", "instances": 10816, "metric_value": 177.0934, "depth": 3}
         if obj[45]<=4.0:
            # {"feature": "C_906170", "instances": 5507, "metric_value": 130.6026, "depth": 4}
            if obj[26]>1.0:
               # {"feature": "C_906370", "instances": 3119, "metric_value": 94.0122, "depth": 5}
               if obj[33]>9.902853478679063:
                  return 'G'
               elif obj[33]<=9.902853478679063:
                  return 'G'
               else:
                  return 'G'
            elif obj[26]<=1.0:
               # {"feature": "C_906370", "instances": 2388, "metric_value": 90.6948, "depth": 5}
               if obj[33]>10.067001675041876:
                  return 'G'
               elif obj[33]<=10.067001675041876:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[45]>4.0:
            # {"feature": "C_906170", "instances": 5309, "metric_value": 120.2015, "depth": 4}
            if obj[26]>2.0:
               # {"feature": "C_906370", "instances": 2899, "metric_value": 83.6308, "depth": 5}
               if obj[33]>17.966885132804414:
                  return 'G'
               elif obj[33]<=17.966885132804414:
                  return 'G'
               else:
                  return 'G'
            elif obj[26]<=2.0:
               # {"feature": "C_999032", "instances": 2410, "metric_value": 86.4608, "depth": 5}
               if obj[35]>0.0:
                  return 'G'
               elif obj[35]<=0.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[34]<=0.0:
         # {"feature": "C_116000", "instances": 10736, "metric_value": 198.5957, "depth": 3}
         if obj[45]>3.0:
            # {"feature": "C_114100", "instances": 5536, "metric_value": 140.7934, "depth": 4}
            if obj[41]>0.7154539197976879:
               # {"feature": "C_906370", "instances": 3060, "metric_value": 103.7084, "depth": 5}
               if obj[33]>17.958823529411763:
                  return 'G'
               elif obj[33]<=17.958823529411763:
                  return 'G'
               else:
                  return 'G'
            elif obj[41]<=0.7154539197976879:
               # {"feature": "C_100100", "instances": 2476, "metric_value": 95.4205, "depth": 5}
               if obj[12]>1.0:
                  return 'G'
               elif obj[12]<=1.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[45]<=3.0:
            # {"feature": "C_906370", "instances": 5200, "metric_value": 139.9509, "depth": 4}
            if obj[33]<=8.634230769230768:
               # {"feature": "C_650640", "instances": 2611, "metric_value": 99.0713, "depth": 5}
               if obj[25]<=2456.9199540405975:
                  return 'G'
               elif obj[25]>2456.9199540405975:
                  return 'G'
               else:
                  return 'G'
            elif obj[33]>8.634230769230768:
               # {"feature": "C_102800", "instances": 2589, "metric_value": 98.8546, "depth": 5}
               if obj[28]<=16.491181923522596:
                  return 'G'
               elif obj[28]>16.491181923522596:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      else:
         return 'G'
   elif obj[0] == '00010':
      # {"feature": "C_660570", "instances": 15971, "metric_value": 448.488, "depth": 2}
      if obj[1] == '00010':
         # {"feature": "C_961223", "instances": 8351, "metric_value": 170.0578, "depth": 3}
         if obj[43]>-18.081426176505794:
            # {"feature": "C_906370", "instances": 4287, "metric_value": 119.831, "depth": 4}
            if obj[33]>0.0:
               # {"feature": "C_114100", "instances": 2306, "metric_value": 82.0808, "depth": 5}
               if obj[41]>0.7329614050303556:
                  return 'G'
               elif obj[41]<=0.7329614050303556:
                  return 'G'
               else:
                  return 'G'
            elif obj[33]<=0.0:
               # {"feature": "C_114100", "instances": 1981, "metric_value": 87.3794, "depth": 5}
               if obj[41]<=0.20597556789500254:
                  return 'G'
               elif obj[41]>0.20597556789500254:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[43]<=-18.081426176505794:
            # {"feature": "C_116000", "instances": 4064, "metric_value": 120.9279, "depth": 4}
            if obj[45]>0.0:
               # {"feature": "C_751200", "instances": 2175, "metric_value": 86.7194, "depth": 5}
               if obj[22]<=0.0:
                  return 'G'
               elif obj[22]>0.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[45]<=0.0:
               # {"feature": "C_110720", "instances": 1889, "metric_value": 84.2997, "depth": 5}
               if obj[32]<=5.678136580201165:
                  return 'G'
               elif obj[32]>5.678136580201165:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '10010':
         # {"feature": "C_111660", "instances": 4584, "metric_value": 125.9743, "depth": 3}
         if obj[8]>-1.0:
            # {"feature": "C_650640", "instances": 2303, "metric_value": 84.6054, "depth": 4}
            if obj[25]<=1946.2492401215804:
               # {"feature": "C_114100", "instances": 1379, "metric_value": 61.097, "depth": 5}
               if obj[41]>0.5928239303843366:
                  return 'G'
               elif obj[41]<=0.5928239303843366:
                  return 'G'
               else:
                  return 'G'
            elif obj[25]>1946.2492401215804:
               # {"feature": "C_100120", "instances": 924, "metric_value": 58.954, "depth": 5}
               if obj[14]<=1.0:
                  return 'G'
               elif obj[14]>1.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[8]<=-1.0:
            # {"feature": "C_752400", "instances": 2281, "metric_value": 93.831, "depth": 4}
            if obj[23]>0.0:
               # {"feature": "C_110720", "instances": 1178, "metric_value": 67.4844, "depth": 5}
               if obj[32]<=6.943123938879457:
                  return 'G'
               elif obj[32]>6.943123938879457:
                  return 'G'
               else:
                  return 'G'
            elif obj[23]<=0.0:
               # {"feature": "C_110720", "instances": 1103, "metric_value": 65.1719, "depth": 5}
               if obj[32]<=5.747053490480508:
                  return 'G'
               elif obj[32]>5.747053490480508:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '10011':
         # {"feature": "C_110720", "instances": 617, "metric_value": 45.9784, "depth": 3}
         if obj[32]<=7.168557536466775:
            # {"feature": "C_107480", "instances": 357, "metric_value": 33.8079, "depth": 4}
            if obj[31]<=58.893837535014:
               # {"feature": "C_104320", "instances": 212, "metric_value": 24.8261, "depth": 5}
               if obj[17]<=67.41037735849056:
                  return 'G'
               elif obj[17]>67.41037735849056:
                  return 'G'
               else:
                  return 'G'
            elif obj[31]>58.893837535014:
               # {"feature": "C_111660", "instances": 145, "metric_value": 23.1046, "depth": 5}
               if obj[8]>-1.0:
                  return 'G'
               elif obj[8]<=-1.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[32]>7.168557536466775:
            # {"feature": "C_100120", "instances": 260, "metric_value": 31.269, "depth": 4}
            if obj[14]<=1.0:
               # {"feature": "C_111660", "instances": 140, "metric_value": 22.321, "depth": 5}
               if obj[8]>-1.0:
                  return 'G'
               elif obj[8]<=-1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[14]>1.0:
               return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '00110':
         # {"feature": "C_111660", "instances": 512, "metric_value": 42.8084, "depth": 3}
         if obj[8]>-1.0:
            # {"feature": "C_111600", "instances": 277, "metric_value": 30.4273, "depth": 4}
            if obj[48]>-1.0:
               # {"feature": "C_999032", "instances": 149, "metric_value": 21.5177, "depth": 5}
               if obj[35]>0.0:
                  return 'G'
               elif obj[35]<=0.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[48]<=-1.0:
               # {"feature": "C_107480", "instances": 128, "metric_value": 21.5609, "depth": 5}
               if obj[31]<=86.67890625000001:
                  return 'G'
               elif obj[31]>86.67890625000001:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[8]<=-1.0:
            # {"feature": "C_650640", "instances": 235, "metric_value": 30.1302, "depth": 4}
            if obj[25]>2548.676595744681:
               return 'G'
            elif obj[25]<=2548.676595744681:
               # {"feature": "C_110720", "instances": 115, "metric_value": 20.7122, "depth": 5}
               if obj[32]>3.0:
                  return 'G'
               elif obj[32]<=3.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '00011':
         # {"feature": "C_111660", "instances": 497, "metric_value": 41.5874, "depth": 3}
         if obj[8]>-1.0:
            # {"feature": "C_650640", "instances": 272, "metric_value": 29.3898, "depth": 4}
            if obj[25]<=4390.327205882353:
               # {"feature": "C_107480", "instances": 156, "metric_value": 21.2032, "depth": 5}
               if obj[31]<=67.35128205128204:
                  return 'G'
               elif obj[31]>67.35128205128204:
                  return 'G'
               else:
                  return 'G'
            elif obj[25]>4390.327205882353:
               # {"feature": "C_100000", "instances": 116, "metric_value": 20.4352, "depth": 5}
               if obj[18]>2.0:
                  return 'G'
               elif obj[18]<=2.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[8]<=-1.0:
            # {"feature": "C_110720", "instances": 225, "metric_value": 29.4678, "depth": 4}
            if obj[32]>6.924444444444444:
               # {"feature": "C_104320", "instances": 113, "metric_value": 20.5166, "depth": 5}
               if obj[17]<=125.04424778761062:
                  return 'G'
               elif obj[17]>125.04424778761062:
                  return 'G'
               else:
                  return 'G'
            elif obj[32]<=6.924444444444444:
               return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '10110':
         # {"feature": "C_650640", "instances": 410, "metric_value": 37.5763, "depth": 3}
         if obj[25]<=2227.741463414634:
            # {"feature": "C_114100", "instances": 217, "metric_value": 26.0415, "depth": 4}
            if obj[41]>0.5615580645161291:
               # {"feature": "C_110720", "instances": 122, "metric_value": 17.9377, "depth": 5}
               if obj[32]<=6.0:
                  return 'G'
               elif obj[32]>6.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[41]<=0.5615580645161291:
               # {"feature": "C_999032", "instances": 95, "metric_value": 19.0843, "depth": 5}
               if obj[35]<=0.0:
                  return 'G'
               elif obj[35]>0.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[25]>2227.741463414634:
            # {"feature": "C_750600", "instances": 193, "metric_value": 27.2135, "depth": 4}
            if obj[21]<=1.0:
               # {"feature": "C_600160", "instances": 102, "metric_value": 19.4187, "depth": 5}
               if obj[42]<=25.5:
                  return 'G'
               elif obj[42]>25.5:
                  return 'G'
               else:
                  return 'G'
            elif obj[21]>1.0:
               return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '01010':
         # {"feature": "C_110720", "instances": 369, "metric_value": 37.7943, "depth": 3}
         if obj[32]>6.86449864498645:
            # {"feature": "C_104320", "instances": 185, "metric_value": 26.6163, "depth": 4}
            if obj[17]>226.8918918918919:
               # {"feature": "C_111660", "instances": 93, "metric_value": 18.4736, "depth": 5}
               if obj[8]>-1.0:
                  return 'G'
               elif obj[8]<=-1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[17]<=226.8918918918919:
               return 'G'
            else:
               return 'G'
         elif obj[32]<=6.86449864498645:
            # {"feature": "C_107480", "instances": 184, "metric_value": 26.836, "depth": 4}
            if obj[31]<=171.42717391304348:
               # {"feature": "C_111500", "instances": 94, "metric_value": 18.9517, "depth": 5}
               if obj[24]>-1.0:
                  return 'G'
               elif obj[24]<=-1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[31]>171.42717391304348:
               return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '11010':
         return 'G'
      elif obj[1] == '10111':
         # {"feature": "C_502400", "instances": 96, "metric_value": 19.5355, "depth": 3}
         if obj[5] == 'G':
            return 'G'
         elif obj[5] == 'B':
            # {"feature": "C_106860", "instances": 16, "metric_value": 7.5485, "depth": 4}
            if obj[9]<=1.0:
               return 'G'
            elif obj[9]>1.0:
               return 'B'
            else:
               return 'G'
         elif obj[5] == 'I':
            return 'G'
         else:
            return 'G'
      elif obj[1] == '01110':
         # {"feature": "C_990660", "instances": 68, "metric_value": 15.5464, "depth": 3}
         if obj[46]<=-71.38941176470587:
            # {"feature": "C_110720", "instances": 37, "metric_value": 10.9044, "depth": 4}
            if obj[32]<=6.0:
               # {"feature": "C_650640", "instances": 22, "metric_value": 7.7796, "depth": 5}
               if obj[25]<=5847.0:
                  return 'G'
               elif obj[25]>5847.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[32]>6.0:
               return 'G'
            else:
               return 'G'
         elif obj[46]>-71.38941176470587:
            return 'G'
         else:
            return 'G'
      elif obj[1] == '00111':
         # {"feature": "C_110720", "instances": 64, "metric_value": 15.0208, "depth": 3}
         if obj[32]<=6.0:
            # {"feature": "C_752400", "instances": 37, "metric_value": 10.9032, "depth": 4}
            if obj[23]>1.0:
               # {"feature": "C_104320", "instances": 21, "metric_value": 7.5301, "depth": 5}
               if obj[17]<=122.0:
                  return 'G'
               elif obj[17]>122.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[23]<=1.0:
               return 'G'
            else:
               return 'G'
         elif obj[32]>6.0:
            return 'G'
         else:
            return 'G'
      elif obj[1] == '01011':
         return 'G'
      elif obj[1] == '11110':
         # {"feature": "C_100000", "instances": 47, "metric_value": 12.5824, "depth": 3}
         if obj[18]<=5.0:
            # {"feature": "C_111660", "instances": 26, "metric_value": 8.6786, "depth": 4}
            if obj[8]>-1.0:
               # {"feature": "C_500300", "instances": 14, "metric_value": 5.7288, "depth": 5}
               if obj[2] == 'G':
                  return 'G'
               elif obj[2] == 'I':
                  return 'B'
               else:
                  return 'G'
            elif obj[8]<=-1.0:
               return 'G'
            else:
               return 'G'
         elif obj[18]>5.0:
            return 'G'
         else:
            return 'G'
      elif obj[1] == '11011':
         # {"feature": "C_650640", "instances": 46, "metric_value": 12.4263, "depth": 3}
         if obj[25]<=8447.347826086956:
            # {"feature": "C_502400", "instances": 26, "metric_value": 9.8939, "depth": 4}
            if obj[5] == 'G':
               # {"feature": "C_104320", "instances": 22, "metric_value": 8.5572, "depth": 5}
               if obj[17]<=212.0:
                  return 'G'
               elif obj[17]>212.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[5] == 'B':
               return 'G'
            elif obj[5] == 'I':
               return 'B'
            else:
               return 'G'
         elif obj[25]>8447.347826086956:
            return 'G'
         else:
            return 'G'
      elif obj[1] == '11111':
         return 'G'
      elif obj[1] == '01111':
         return 'G'
      else:
         return 'G'
   elif obj[0] == '11000':
      # {"feature": "C_660570", "instances": 15904, "metric_value": 350.4688, "depth": 2}
      if obj[1] == '11000':
         # {"feature": "C_752400", "instances": 10302, "metric_value": 188.7286, "depth": 3}
         if obj[23]>1.0:
            # {"feature": "C_104320", "instances": 5379, "metric_value": 133.9051, "depth": 4}
            if obj[17]>132.9524075106897:
               # {"feature": "C_114100", "instances": 2832, "metric_value": 92.0982, "depth": 5}
               if obj[41]>0.6403572740112995:
                  return 'G'
               elif obj[41]<=0.6403572740112995:
                  return 'G'
               else:
                  return 'G'
            elif obj[17]<=132.9524075106897:
               # {"feature": "C_114100", "instances": 2547, "metric_value": 97.3504, "depth": 5}
               if obj[41]>0.9192378091872793:
                  return 'G'
               elif obj[41]<=0.9192378091872793:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[23]<=1.0:
            # {"feature": "C_600160", "instances": 4923, "metric_value": 133.0515, "depth": 4}
            if obj[42]>-1.0:
               # {"feature": "C_906370", "instances": 2712, "metric_value": 97.7757, "depth": 5}
               if obj[33]>9.549041297935103:
                  return 'G'
               elif obj[33]<=9.549041297935103:
                  return 'G'
               else:
                  return 'G'
            elif obj[42]<=-1.0:
               # {"feature": "C_751200", "instances": 2211, "metric_value": 90.3991, "depth": 5}
               if obj[22]>1.0:
                  return 'G'
               elif obj[22]<=1.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '11011':
         # {"feature": "C_104320", "instances": 2343, "metric_value": 90.7323, "depth": 3}
         if obj[17]>137.07682458386682:
            # {"feature": "C_502400", "instances": 1228, "metric_value": 65.4759, "depth": 4}
            if obj[5] == 'G':
               # {"feature": "C_114100", "instances": 928, "metric_value": 59.8744, "depth": 5}
               if obj[41]>0.7016743534482759:
                  return 'G'
               elif obj[41]<=0.7016743534482759:
                  return 'G'
               else:
                  return 'G'
            elif obj[5] == 'B':
               # {"feature": "C_501200", "instances": 194, "metric_value": 22.72, "depth": 5}
               if obj[4] == 'B':
                  return 'G'
               elif obj[4] == 'G':
                  return 'G'
               elif obj[4] == 'I':
                  return 'G'
               else:
                  return 'G'
            elif obj[5] == 'I':
               # {"feature": "C_750100", "instances": 106, "metric_value": 15.7019, "depth": 5}
               if obj[19]<=3.0:
                  return 'G'
               elif obj[19]>3.0:
                  return 'B'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[17]<=137.07682458386682:
            # {"feature": "C_906370", "instances": 1115, "metric_value": 64.4765, "depth": 4}
            if obj[33]>10.79103139013453:
               # {"feature": "C_102800", "instances": 600, "metric_value": 47.0171, "depth": 5}
               if obj[28]<=16.32678333333333:
                  return 'G'
               elif obj[28]>16.32678333333333:
                  return 'G'
               else:
                  return 'G'
            elif obj[33]<=10.79103139013453:
               # {"feature": "C_106600", "instances": 515, "metric_value": 44.1571, "depth": 5}
               if obj[37]<=0.0:
                  return 'G'
               elif obj[37]>0.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '11100':
         # {"feature": "C_906370", "instances": 1306, "metric_value": 66.6309, "depth": 3}
         if obj[33]>10.480857580398162:
            # {"feature": "C_102800", "instances": 672, "metric_value": 47.5797, "depth": 4}
            if obj[28]<=17.951383928571428:
               # {"feature": "C_106860", "instances": 385, "metric_value": 34.4325, "depth": 5}
               if obj[9]>2.0:
                  return 'G'
               elif obj[9]<=2.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[28]>17.951383928571428:
               # {"feature": "C_100120", "instances": 287, "metric_value": 32.9489, "depth": 5}
               if obj[14]>2.0:
                  return 'G'
               elif obj[14]<=2.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[33]<=10.480857580398162:
            # {"feature": "C_104320", "instances": 634, "metric_value": 46.7859, "depth": 4}
            if obj[17]>138.1608832807571:
               # {"feature": "C_107480", "instances": 340, "metric_value": 32.1845, "depth": 5}
               if obj[31]<=76.91852941176471:
                  return 'G'
               elif obj[31]>76.91852941176471:
                  return 'G'
               else:
                  return 'G'
            elif obj[17]<=138.1608832807571:
               # {"feature": "C_600160", "instances": 294, "metric_value": 34.0602, "depth": 5}
               if obj[42]>19.496598639455783:
                  return 'G'
               elif obj[42]<=19.496598639455783:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '11010':
         # {"feature": "C_502400", "instances": 1288, "metric_value": 70.9864, "depth": 3}
         if obj[5] == 'G':
            # {"feature": "C_104320", "instances": 936, "metric_value": 58.819, "depth": 4}
            if obj[17]>157.70405982905982:
               # {"feature": "C_114100", "instances": 532, "metric_value": 43.195, "depth": 5}
               if obj[41]>0.7011490601503759:
                  return 'G'
               elif obj[41]<=0.7011490601503759:
                  return 'G'
               else:
                  return 'G'
            elif obj[17]<=157.70405982905982:
               # {"feature": "C_752400", "instances": 404, "metric_value": 40.0009, "depth": 5}
               if obj[23]>1.0:
                  return 'G'
               elif obj[23]<=1.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[5] == 'B':
            # {"feature": "C_501200", "instances": 253, "metric_value": 26.2794, "depth": 4}
            if obj[4] == 'B':
               # {"feature": "C_500600", "instances": 134, "metric_value": 19.2152, "depth": 5}
               if obj[3] == 'G':
                  return 'G'
               elif obj[3] == 'B':
                  return 'G'
               elif obj[3] == 'I':
                  return 'G'
               else:
                  return 'G'
            elif obj[4] == 'G':
               # {"feature": "C_107480", "instances": 108, "metric_value": 19.657, "depth": 5}
               if obj[31]<=83.68796296296294:
                  return 'G'
               elif obj[31]>83.68796296296294:
                  return 'G'
               else:
                  return 'G'
            elif obj[4] == 'I':
               # {"feature": "C_111500", "instances": 11, "metric_value": 4.4495, "depth": 5}
               if obj[24]<=9.0:
                  return 'G'
               elif obj[24]>9.0:
                  return 'B'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[5] == 'I':
            # {"feature": "C_110720", "instances": 99, "metric_value": 16.493, "depth": 4}
            if obj[32]<=19.0:
               # {"feature": "C_111600", "instances": 59, "metric_value": 11.051, "depth": 5}
               if obj[48]<=0.0:
                  return 'G'
               elif obj[48]>0.0:
                  return 'B'
               else:
                  return 'G'
            elif obj[32]>19.0:
               return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '11111':
         # {"feature": "C_502400", "instances": 378, "metric_value": 37.2839, "depth": 3}
         if obj[5] == 'G':
            # {"feature": "C_104320", "instances": 304, "metric_value": 34.415, "depth": 4}
            if obj[17]>140.8453947368421:
               # {"feature": "C_100120", "instances": 157, "metric_value": 24.4282, "depth": 5}
               if obj[14]>4.0:
                  return 'G'
               elif obj[14]<=4.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[17]<=140.8453947368421:
               return 'G'
            else:
               return 'G'
         elif obj[5] == 'B':
            # {"feature": "C_500600", "instances": 41, "metric_value": 12.6418, "depth": 4}
            if obj[3] == 'G':
               # {"feature": "C_501200", "instances": 27, "metric_value": 11.2469, "depth": 5}
               if obj[4] == 'G':
                  return 'G'
               elif obj[4] == 'B':
                  return 'G'
               elif obj[4] == 'I':
                  return 'G'
               else:
                  return 'G'
            elif obj[3] == 'B':
               # {"feature": "C_500300", "instances": 11, "metric_value": 7.0711, "depth": 5}
               if obj[2] == 'G':
                  return 'G'
               elif obj[2] == 'B':
                  return 'G'
               elif obj[2] == 'I':
                  return 'B'
               else:
                  return 'G'
            elif obj[3] == 'I':
               return 'B'
            else:
               return 'G'
         elif obj[5] == 'I':
            # {"feature": "C_600160", "instances": 33, "metric_value": 8.3086, "depth": 4}
            if obj[42]>19.0:
               # {"feature": "C_116000", "instances": 22, "metric_value": 6.0809, "depth": 5}
               if obj[45]<=4.0:
                  return 'G'
               elif obj[45]>4.0:
                  return 'B'
               else:
                  return 'G'
            elif obj[42]<=19.0:
               return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '11110':
         # {"feature": "C_502400", "instances": 209, "metric_value": 24.3165, "depth": 3}
         if obj[5] == 'G':
            # {"feature": "C_116000", "instances": 141, "metric_value": 23.0838, "depth": 4}
            if obj[45]>2.0:
               # {"feature": "C_100120", "instances": 74, "metric_value": 16.2961, "depth": 5}
               if obj[14]>5.0:
                  return 'G'
               elif obj[14]<=5.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[45]<=2.0:
               return 'G'
            else:
               return 'G'
         elif obj[5] == 'B':
            # {"feature": "C_500600", "instances": 50, "metric_value": 9.8455, "depth": 4}
            if obj[3] == 'G':
               # {"feature": "C_501200", "instances": 24, "metric_value": 9.3706, "depth": 5}
               if obj[4] == 'B':
                  return 'G'
               elif obj[4] == 'G':
                  return 'G'
               elif obj[4] == 'I':
                  return 'G'
               else:
                  return 'G'
            elif obj[3] == 'B':
               # {"feature": "C_106880", "instances": 17, "metric_value": 5.4732, "depth": 5}
               if obj[10]<=5.0:
                  return 'G'
               elif obj[10]>5.0:
                  return 'B'
               else:
                  return 'G'
            elif obj[3] == 'I':
               # {"feature": "C_106920", "instances": 9, "metric_value": 5.7417, "depth": 5}
               if obj[11]<=1.0:
                  return 'B'
               elif obj[11]>1.0:
                  return 'G'
               else:
                  return 'B'
            else:
               return 'G'
         elif obj[5] == 'I':
            # {"feature": "C_906370", "instances": 18, "metric_value": 6.9497, "depth": 4}
            if obj[33]<=18.0:
               # {"feature": "C_501200", "instances": 16, "metric_value": 7.0418, "depth": 5}
               if obj[4] == 'I':
                  return 'G'
               elif obj[4] == 'G':
                  return 'G'
               else:
                  return 'G'
            elif obj[33]>18.0:
               return 'B'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '11001':
         return 'G'
      elif obj[1] == '11101':
         return 'G'
      else:
         return 'G'
   elif obj[0] == '11010':
      # {"feature": "C_660570", "instances": 15116, "metric_value": 281.9839, "depth": 2}
      if obj[1] == '11010':
         # {"feature": "C_752400", "instances": 10758, "metric_value": 194.7942, "depth": 3}
         if obj[23]>1.0:
            # {"feature": "C_104320", "instances": 5392, "metric_value": 136.6138, "depth": 4}
            if obj[17]>159.36350148367953:
               # {"feature": "C_114100", "instances": 3008, "metric_value": 100.1219, "depth": 5}
               if obj[41]>0.6684173204787234:
                  return 'G'
               elif obj[41]<=0.6684173204787234:
                  return 'G'
               else:
                  return 'G'
            elif obj[17]<=159.36350148367953:
               # {"feature": "C_116000", "instances": 2384, "metric_value": 93.0679, "depth": 5}
               if obj[45]>3.0:
                  return 'G'
               elif obj[45]<=3.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[23]<=1.0:
            # {"feature": "C_906370", "instances": 5366, "metric_value": 138.8216, "depth": 4}
            if obj[33]>11.425083861349236:
               # {"feature": "C_600160", "instances": 2712, "metric_value": 96.4602, "depth": 5}
               if obj[42]<=18.432153392330385:
                  return 'G'
               elif obj[42]>18.432153392330385:
                  return 'G'
               else:
                  return 'G'
            elif obj[33]<=11.425083861349236:
               # {"feature": "C_650640", "instances": 2654, "metric_value": 99.8497, "depth": 5}
               if obj[25]>2487.882064807837:
                  return 'G'
               elif obj[25]<=2487.882064807837:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '11011':
         # {"feature": "C_116000", "instances": 1964, "metric_value": 82.6954, "depth": 3}
         if obj[45]>3.0:
            # {"feature": "C_999032", "instances": 1016, "metric_value": 58.2371, "depth": 4}
            if obj[35]>0.0:
               # {"feature": "C_100000", "instances": 520, "metric_value": 40.8843, "depth": 5}
               if obj[18]<=9.0:
                  return 'G'
               elif obj[18]>9.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[35]<=0.0:
               # {"feature": "C_100120", "instances": 496, "metric_value": 41.4905, "depth": 5}
               if obj[14]<=4.0:
                  return 'G'
               elif obj[14]>4.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[45]<=3.0:
            # {"feature": "C_100000", "instances": 948, "metric_value": 58.7188, "depth": 4}
            if obj[18]<=6.0:
               # {"feature": "C_600160", "instances": 479, "metric_value": 41.9786, "depth": 5}
               if obj[42]<=14.707724425887266:
                  return 'G'
               elif obj[42]>14.707724425887266:
                  return 'G'
               else:
                  return 'G'
            elif obj[18]>6.0:
               # {"feature": "C_100140", "instances": 469, "metric_value": 41.1016, "depth": 5}
               if obj[15]<=2.0:
                  return 'G'
               elif obj[15]>2.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '11110':
         # {"feature": "C_116000", "instances": 1930, "metric_value": 81.8647, "depth": 3}
         if obj[45]>3.0:
            # {"feature": "C_106880", "instances": 1057, "metric_value": 57.7772, "depth": 4}
            if obj[10]>2.0:
               # {"feature": "C_106860", "instances": 564, "metric_value": 41.333, "depth": 5}
               if obj[9]>3.0:
                  return 'G'
               elif obj[9]<=3.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[10]<=2.0:
               # {"feature": "C_600160", "instances": 493, "metric_value": 40.4429, "depth": 5}
               if obj[42]>19.829614604462474:
                  return 'G'
               elif obj[42]<=19.829614604462474:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[45]<=3.0:
            # {"feature": "C_104320", "instances": 873, "metric_value": 58.0118, "depth": 4}
            if obj[17]>151.11340206185568:
               # {"feature": "C_100120", "instances": 448, "metric_value": 41.1981, "depth": 5}
               if obj[14]>2.0:
                  return 'G'
               elif obj[14]<=2.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[17]<=151.11340206185568:
               # {"feature": "C_906370", "instances": 425, "metric_value": 40.829, "depth": 5}
               if obj[33]>11.409411764705883:
                  return 'G'
               elif obj[33]<=11.409411764705883:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '11111':
         # {"feature": "C_116000", "instances": 464, "metric_value": 39.5764, "depth": 3}
         if obj[45]>3.0:
            # {"feature": "C_100000", "instances": 269, "metric_value": 29.0323, "depth": 4}
            if obj[18]>10.0:
               # {"feature": "C_650640", "instances": 158, "metric_value": 20.4866, "depth": 5}
               if obj[25]<=7162.101265822785:
                  return 'G'
               elif obj[25]>7162.101265822785:
                  return 'G'
               else:
                  return 'G'
            elif obj[18]<=10.0:
               # {"feature": "C_999032", "instances": 111, "metric_value": 20.6947, "depth": 5}
               if obj[35]>0.0:
                  return 'G'
               elif obj[35]<=0.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[45]<=3.0:
            # {"feature": "C_906370", "instances": 195, "metric_value": 27.0713, "depth": 4}
            if obj[33]>10.846153846153847:
               # {"feature": "C_102800", "instances": 108, "metric_value": 19.6576, "depth": 5}
               if obj[28]>11.11:
                  return 'G'
               elif obj[28]<=11.11:
                  return 'G'
               else:
                  return 'G'
            elif obj[33]<=10.846153846153847:
               return 'G'
            else:
               return 'G'
         else:
            return 'G'
      else:
         return 'G'
   elif obj[0] == '01000':
      # {"feature": "C_660570", "instances": 12205, "metric_value": 438.0328, "depth": 2}
      if obj[1] == '01000':
         # {"feature": "C_111500", "instances": 5285, "metric_value": 140.0757, "depth": 3}
         if obj[24]<=-1.0:
            # {"feature": "C_114900", "instances": 3117, "metric_value": 110.861, "depth": 4}
            if obj[49]<=390.5245428296439:
               # {"feature": "C_999032", "instances": 1778, "metric_value": 82.6022, "depth": 5}
               if obj[35]<=0.0:
                  return 'G'
               elif obj[35]>0.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[49]>390.5245428296439:
               # {"feature": "C_999032", "instances": 1339, "metric_value": 71.7918, "depth": 5}
               if obj[35]<=0.0:
                  return 'G'
               elif obj[35]>0.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[24]>-1.0:
            # {"feature": "C_104320", "instances": 2168, "metric_value": 86.4884, "depth": 4}
            if obj[17]<=108.98939114391143:
               # {"feature": "C_114900", "instances": 1204, "metric_value": 68.5948, "depth": 5}
               if obj[49]>335.8887043189369:
                  return 'G'
               elif obj[49]<=335.8887043189369:
                  return 'G'
               else:
                  return 'G'
            elif obj[17]>108.98939114391143:
               # {"feature": "C_906370", "instances": 964, "metric_value": 53.8542, "depth": 5}
               if obj[33]>2.0:
                  return 'G'
               elif obj[33]<=2.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '11000':
         # {"feature": "C_751200", "instances": 3144, "metric_value": 107.9859, "depth": 3}
         if obj[22]>1.0:
            # {"feature": "C_100120", "instances": 1711, "metric_value": 77.2172, "depth": 4}
            if obj[14]<=1.0:
               # {"feature": "C_104320", "instances": 859, "metric_value": 54.3962, "depth": 5}
               if obj[17]>127.27008149010477:
                  return 'G'
               elif obj[17]<=127.27008149010477:
                  return 'G'
               else:
                  return 'G'
            elif obj[14]>1.0:
               # {"feature": "C_750100", "instances": 852, "metric_value": 54.8701, "depth": 5}
               if obj[19]>1.0:
                  return 'G'
               elif obj[19]<=1.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[22]<=1.0:
            # {"feature": "C_752400", "instances": 1433, "metric_value": 75.4856, "depth": 4}
            if obj[23]<=0.0:
               # {"feature": "C_114900", "instances": 743, "metric_value": 54.3395, "depth": 5}
               if obj[49]<=407.4495289367429:
                  return 'G'
               elif obj[49]>407.4495289367429:
                  return 'G'
               else:
                  return 'G'
            elif obj[23]>0.0:
               # {"feature": "C_102800", "instances": 690, "metric_value": 52.3827, "depth": 5}
               if obj[28]>40.0:
                  return 'G'
               elif obj[28]<=40.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '11011':
         # {"feature": "C_502400", "instances": 692, "metric_value": 52.6771, "depth": 3}
         if obj[5] == 'G':
            # {"feature": "C_750600", "instances": 551, "metric_value": 46.2651, "depth": 4}
            if obj[21]<=1.0:
               # {"feature": "C_102800", "instances": 276, "metric_value": 32.7199, "depth": 5}
               if obj[28]<=25.0:
                  return 'G'
               elif obj[28]>25.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[21]>1.0:
               # {"feature": "C_103380", "instances": 275, "metric_value": 32.6868, "depth": 5}
               if obj[36]<=28.57:
                  return 'G'
               elif obj[36]>28.57:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[5] == 'B':
            # {"feature": "C_501200", "instances": 113, "metric_value": 19.7307, "depth": 4}
            if obj[4] == 'B':
               # {"feature": "C_500600", "instances": 62, "metric_value": 16.8922, "depth": 5}
               if obj[3] == 'B':
                  return 'G'
               elif obj[3] == 'G':
                  return 'G'
               elif obj[3] == 'I':
                  return 'G'
               else:
                  return 'G'
            elif obj[4] == 'G':
               # {"feature": "C_111620", "instances": 44, "metric_value": 12.6754, "depth": 5}
               if obj[6]>-1.0:
                  return 'G'
               elif obj[6]<=-1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[4] == 'I':
               # {"feature": "C_500300", "instances": 6, "metric_value": 4.899, "depth": 5}
               if obj[2] == 'G':
                  return 'G'
               elif obj[2] == 'I':
                  return 'B'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[5] == 'I':
            # {"feature": "C_501200", "instances": 27, "metric_value": 8.9331, "depth": 4}
            if obj[4] == 'I':
               # {"feature": "C_106860", "instances": 16, "metric_value": 6.1611, "depth": 5}
               if obj[9]<=1.0:
                  return 'G'
               elif obj[9]>1.0:
                  return 'B'
               else:
                  return 'G'
            elif obj[4] == 'G':
               return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '01011':
         # {"feature": "C_111640", "instances": 620, "metric_value": 47.9004, "depth": 3}
         if obj[7]>-1.0:
            # {"feature": "C_100000", "instances": 340, "metric_value": 34.2815, "depth": 4}
            if obj[18]>2.0:
               # {"feature": "C_114100", "instances": 188, "metric_value": 24.8631, "depth": 5}
               if obj[41]>0.7236367021276596:
                  return 'G'
               elif obj[41]<=0.7236367021276596:
                  return 'G'
               else:
                  return 'G'
            elif obj[18]<=2.0:
               # {"feature": "C_752400", "instances": 152, "metric_value": 23.6777, "depth": 5}
               if obj[23]>1.0:
                  return 'G'
               elif obj[23]<=1.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[7]<=-1.0:
            return 'G'
         else:
            return 'G'
      elif obj[1] == '01010':
         # {"feature": "C_111660", "instances": 588, "metric_value": 47.0141, "depth": 3}
         if obj[8]>-1.0:
            # {"feature": "C_502400", "instances": 319, "metric_value": 34.0401, "depth": 4}
            if obj[5] == 'G':
               # {"feature": "C_110720", "instances": 250, "metric_value": 30.8708, "depth": 5}
               if obj[32]<=8.748:
                  return 'G'
               elif obj[32]>8.748:
                  return 'G'
               else:
                  return 'G'
            elif obj[5] == 'B':
               # {"feature": "C_501200", "instances": 60, "metric_value": 15.2179, "depth": 5}
               if obj[4] == 'B':
                  return 'G'
               elif obj[4] == 'G':
                  return 'G'
               elif obj[4] == 'I':
                  return 'G'
               else:
                  return 'G'
            elif obj[5] == 'I':
               # {"feature": "C_750100", "instances": 9, "metric_value": 5.7417, "depth": 5}
               if obj[19]<=4.0:
                  return 'G'
               elif obj[19]>4.0:
                  return 'B'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[8]<=-1.0:
            # {"feature": "C_110720", "instances": 269, "metric_value": 32.5565, "depth": 4}
            if obj[32]<=0.0:
               # {"feature": "C_107480", "instances": 140, "metric_value": 23.328, "depth": 5}
               if obj[31]>119.36142857142859:
                  return 'G'
               elif obj[31]<=119.36142857142859:
                  return 'G'
               else:
                  return 'G'
            elif obj[32]>0.0:
               return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '01100':
         # {"feature": "C_751200", "instances": 578, "metric_value": 46.7489, "depth": 3}
         if obj[22]>1.0:
            # {"feature": "C_750100", "instances": 313, "metric_value": 33.8146, "depth": 4}
            if obj[19]>1.0:
               # {"feature": "C_104320", "instances": 162, "metric_value": 23.5998, "depth": 5}
               if obj[17]>132.90123456790124:
                  return 'G'
               elif obj[17]<=132.90123456790124:
                  return 'G'
               else:
                  return 'G'
            elif obj[19]<=1.0:
               # {"feature": "C_111640", "instances": 151, "metric_value": 24.2464, "depth": 5}
               if obj[7]>-1.0:
                  return 'G'
               elif obj[7]<=-1.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[22]<=1.0:
            # {"feature": "C_111500", "instances": 265, "metric_value": 32.3099, "depth": 4}
            if obj[24]<=-1.0:
               # {"feature": "C_114900", "instances": 138, "metric_value": 23.0644, "depth": 5}
               if obj[49]<=399.05797101449275:
                  return 'G'
               elif obj[49]>399.05797101449275:
                  return 'G'
               else:
                  return 'G'
            elif obj[24]>-1.0:
               return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '11010':
         # {"feature": "C_502400", "instances": 510, "metric_value": 47.3252, "depth": 3}
         if obj[5] == 'G':
            # {"feature": "C_102800", "instances": 322, "metric_value": 35.2204, "depth": 4}
            if obj[28]>28.57:
               # {"feature": "C_110720", "instances": 164, "metric_value": 24.9946, "depth": 5}
               if obj[32]<=0.0:
                  return 'G'
               elif obj[32]>0.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[28]<=28.57:
               # {"feature": "C_111620", "instances": 158, "metric_value": 24.8214, "depth": 5}
               if obj[6]<=-1.0:
                  return 'G'
               elif obj[6]>-1.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[5] == 'B':
            # {"feature": "C_501200", "instances": 161, "metric_value": 25.6235, "depth": 4}
            if obj[4] == 'B':
               # {"feature": "C_500300", "instances": 81, "metric_value": 17.4031, "depth": 5}
               if obj[2] == 'G':
                  return 'G'
               elif obj[2] == 'B':
                  return 'G'
               elif obj[2] == 'I':
                  return 'B'
               else:
                  return 'G'
            elif obj[4] == 'G':
               return 'G'
            elif obj[4] == 'I':
               return 'G'
            else:
               return 'G'
         elif obj[5] == 'I':
            # {"feature": "C_111620", "instances": 27, "metric_value": 9.0711, "depth": 4}
            if obj[6]<=1.0:
               return 'G'
            elif obj[6]>1.0:
               return 'B'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '11100':
         # {"feature": "C_750600", "instances": 349, "metric_value": 36.2924, "depth": 3}
         if obj[21]>1.0:
            # {"feature": "C_502400", "instances": 193, "metric_value": 27.12, "depth": 4}
            if obj[5] == 'G':
               # {"feature": "C_100120", "instances": 154, "metric_value": 24.497, "depth": 5}
               if obj[14]<=1.0:
                  return 'G'
               elif obj[14]>1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[5] == 'B':
               # {"feature": "C_500300", "instances": 27, "metric_value": 9.1877, "depth": 5}
               if obj[2] == 'G':
                  return 'G'
               elif obj[2] == 'B':
                  return 'G'
               elif obj[2] == 'I':
                  return 'B'
               else:
                  return 'G'
            elif obj[5] == 'I':
               # {"feature": "C_104320", "instances": 12, "metric_value": 5.8349, "depth": 5}
               if obj[17]<=185.0:
                  return 'G'
               elif obj[17]>185.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[21]<=1.0:
            return 'G'
         else:
            return 'G'
      elif obj[1] == '11111':
         # {"feature": "C_502400", "instances": 123, "metric_value": 22.6322, "depth": 3}
         if obj[5] == 'G':
            # {"feature": "C_100000", "instances": 100, "metric_value": 19.6038, "depth": 4}
            if obj[18]<=5.0:
               # {"feature": "C_114900", "instances": 52, "metric_value": 13.877, "depth": 5}
               if obj[49]<=408.0:
                  return 'G'
               elif obj[49]>408.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[18]>5.0:
               return 'G'
            else:
               return 'G'
         elif obj[5] == 'B':
            # {"feature": "C_501200", "instances": 12, "metric_value": 7.026, "depth": 4}
            if obj[4] == 'G':
               return 'G'
            elif obj[4] == 'B':
               # {"feature": "C_111640", "instances": 4, "metric_value": 3.8637, "depth": 5}
               if obj[7]<=6.0:
                  return 'G'
               elif obj[7]>6.0:
                  return 'B'
               else:
                  return 'G'
            elif obj[4] == 'I':
               return 'G'
            else:
               return 'G'
         elif obj[5] == 'I':
            return 'G'
         else:
            return 'G'
      elif obj[1] == '11110':
         # {"feature": "C_502400", "instances": 86, "metric_value": 19.2673, "depth": 3}
         if obj[5] == 'G':
            return 'G'
         elif obj[5] == 'B':
            # {"feature": "C_501200", "instances": 20, "metric_value": 8.2434, "depth": 4}
            if obj[4] == 'G':
               return 'G'
            elif obj[4] == 'B':
               # {"feature": "C_106880", "instances": 9, "metric_value": 5.7417, "depth": 5}
               if obj[10]<=5.0:
                  return 'G'
               elif obj[10]>5.0:
                  return 'B'
               else:
                  return 'G'
            elif obj[4] == 'I':
               return 'G'
            else:
               return 'G'
         elif obj[5] == 'I':
            return 'G'
         else:
            return 'G'
      elif obj[1] == '01110':
         return 'G'
      elif obj[1] == '01111':
         # {"feature": "C_104320", "instances": 70, "metric_value": 15.7887, "depth": 3}
         if obj[17]>144.5857142857143:
            # {"feature": "C_111620", "instances": 36, "metric_value": 10.7235, "depth": 4}
            if obj[6]>-1.0:
               # {"feature": "C_105740", "instances": 21, "metric_value": 7.5301, "depth": 5}
               if obj[44]>69.0:
                  return 'G'
               elif obj[44]<=69.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[6]<=-1.0:
               return 'G'
            else:
               return 'G'
         elif obj[17]<=144.5857142857143:
            return 'G'
         else:
            return 'G'
      elif obj[1] == '01001':
         # {"feature": "C_500300", "instances": 39, "metric_value": 10.9658, "depth": 3}
         if obj[2] == 'G':
            # {"feature": "C_104320", "instances": 37, "metric_value": 11.5231, "depth": 4}
            if obj[17]>132.05405405405406:
               # {"feature": "C_111620", "instances": 20, "metric_value": 8.0825, "depth": 5}
               if obj[6]>-1.0:
                  return 'G'
               elif obj[6]<=-1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[17]<=132.05405405405406:
               return 'G'
            else:
               return 'G'
         elif obj[2] == 'B':
            return 'B'
         elif obj[2] == 'I':
            return 'B'
         else:
            return 'G'
      elif obj[1] == '11001':
         return 'G'
      elif obj[1] == '11101':
         # {"feature": "C_500600", "instances": 8, "metric_value": 6.2925, "depth": 3}
         if obj[3] == 'G':
            return 'G'
         elif obj[3] == 'B':
            return 'G'
         elif obj[3] == 'I':
            return 'B'
         else:
            return 'G'
      elif obj[1] == '01101':
         # {"feature": "C_100110", "instances": 2, "metric_value": 2.8284, "depth": 3}
         if obj[13]>1.0:
            return 'G'
         elif obj[13]<=1.0:
            return 'B'
         else:
            return 'G'
      else:
         return 'G'
   elif obj[0] == '10100':
      # {"feature": "C_660570", "instances": 12146, "metric_value": 232.4855, "depth": 2}
      if obj[1] == '10100':
         # {"feature": "C_107480", "instances": 8941, "metric_value": 151.777, "depth": 3}
         if obj[31]<=27.06088804384297:
            # {"feature": "C_752400", "instances": 4629, "metric_value": 107.7512, "depth": 4}
            if obj[23]>0.0:
               # {"feature": "C_116000", "instances": 2504, "metric_value": 75.5835, "depth": 5}
               if obj[45]>2.0:
                  return 'G'
               elif obj[45]<=2.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[23]<=0.0:
               # {"feature": "C_100000", "instances": 2125, "metric_value": 77.1032, "depth": 5}
               if obj[18]>2.0:
                  return 'G'
               elif obj[18]<=2.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[31]>27.06088804384297:
            # {"feature": "C_100110", "instances": 4312, "metric_value": 107.1207, "depth": 4}
            if obj[13]<=1.0:
               # {"feature": "C_114100", "instances": 2390, "metric_value": 76.5815, "depth": 5}
               if obj[41]>0.6291078242677824:
                  return 'G'
               elif obj[41]<=0.6291078242677824:
                  return 'G'
               else:
                  return 'G'
            elif obj[13]>1.0:
               # {"feature": "C_116000", "instances": 1922, "metric_value": 74.8875, "depth": 5}
               if obj[45]<=2.0:
                  return 'G'
               elif obj[45]>2.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '10111':
         # {"feature": "C_502400", "instances": 2203, "metric_value": 68.8662, "depth": 3}
         if obj[5] == 'G':
            # {"feature": "C_107480", "instances": 1545, "metric_value": 68.8386, "depth": 4}
            if obj[31]<=33.11223300970873:
               # {"feature": "C_116000", "instances": 862, "metric_value": 48.9255, "depth": 5}
               if obj[45]>2.0:
                  return 'G'
               elif obj[45]<=2.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[31]>33.11223300970873:
               # {"feature": "C_100110", "instances": 683, "metric_value": 48.4331, "depth": 5}
               if obj[13]<=1.0:
                  return 'G'
               elif obj[13]>1.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[5] == 'B':
            # {"feature": "C_500300", "instances": 367, "metric_value": 27.6455, "depth": 4}
            if obj[2] == 'G':
               # {"feature": "C_501200", "instances": 260, "metric_value": 25.0465, "depth": 5}
               if obj[4] == 'B':
                  return 'G'
               elif obj[4] == 'G':
                  return 'G'
               elif obj[4] == 'I':
                  return 'G'
               else:
                  return 'G'
            elif obj[2] == 'I':
               # {"feature": "C_111300", "instances": 66, "metric_value": 10.909, "depth": 5}
               if obj[38]<=-1.0:
                  return 'B'
               elif obj[38]>-1.0:
                  return 'B'
               else:
                  return 'B'
            elif obj[2] == 'B':
               # {"feature": "C_750100", "instances": 41, "metric_value": 8.8191, "depth": 5}
               if obj[19]<=2.0:
                  return 'G'
               elif obj[19]>2.0:
                  return 'B'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[5] == 'I':
            # {"feature": "C_750100", "instances": 291, "metric_value": 22.6384, "depth": 4}
            if obj[19]<=3.0:
               # {"feature": "C_100000", "instances": 213, "metric_value": 20.9477, "depth": 5}
               if obj[18]<=10.417840375586854:
                  return 'G'
               elif obj[18]>10.417840375586854:
                  return 'G'
               else:
                  return 'G'
            elif obj[19]>3.0:
               # {"feature": "C_750600", "instances": 78, "metric_value": 11.7634, "depth": 5}
               if obj[21]<=2.0:
                  return 'B'
               elif obj[21]>2.0:
                  return 'B'
               else:
                  return 'B'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '10110':
         # {"feature": "C_502400", "instances": 562, "metric_value": 41.1646, "depth": 3}
         if obj[5] == 'G':
            # {"feature": "C_107480", "instances": 311, "metric_value": 31.6834, "depth": 4}
            if obj[31]<=44.41993569131833:
               # {"feature": "C_103380", "instances": 187, "metric_value": 23.3629, "depth": 5}
               if obj[36]>11.11:
                  return 'G'
               elif obj[36]<=11.11:
                  return 'G'
               else:
                  return 'G'
            elif obj[31]>44.41993569131833:
               # {"feature": "C_103380", "instances": 124, "metric_value": 21.5629, "depth": 5}
               if obj[36]<=18.18:
                  return 'G'
               elif obj[36]>18.18:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[5] == 'B':
            # {"feature": "C_501200", "instances": 187, "metric_value": 20.352, "depth": 4}
            if obj[4] == 'B':
               # {"feature": "C_500600", "instances": 91, "metric_value": 13.4523, "depth": 5}
               if obj[3] == 'G':
                  return 'G'
               elif obj[3] == 'B':
                  return 'G'
               elif obj[3] == 'I':
                  return 'G'
               else:
                  return 'G'
            elif obj[4] == 'G':
               # {"feature": "C_752400", "instances": 78, "metric_value": 15.0895, "depth": 5}
               if obj[23]>7.0:
                  return 'G'
               elif obj[23]<=7.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[4] == 'I':
               # {"feature": "C_600160", "instances": 18, "metric_value": 5.7889, "depth": 5}
               if obj[42]>34.0:
                  return 'B'
               elif obj[42]<=34.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[5] == 'I':
            # {"feature": "C_750100", "instances": 64, "metric_value": 10.4352, "depth": 4}
            if obj[19]<=2.0:
               # {"feature": "C_110720", "instances": 49, "metric_value": 11.3191, "depth": 5}
               if obj[32]<=14.0:
                  return 'G'
               elif obj[32]>14.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[19]>2.0:
               # {"feature": "C_930623", "instances": 15, "metric_value": 5.2518, "depth": 5}
               if obj[27]>-7.24:
                  return 'B'
               elif obj[27]<=-7.24:
                  return 'G'
               else:
                  return 'B'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '11100':
         # {"feature": "C_502400", "instances": 190, "metric_value": 27.9439, "depth": 3}
         if obj[5] == 'G':
            # {"feature": "C_100120", "instances": 159, "metric_value": 24.9036, "depth": 4}
            if obj[14]>3.0:
               # {"feature": "C_116000", "instances": 81, "metric_value": 17.5579, "depth": 5}
               if obj[45]>2.0:
                  return 'G'
               elif obj[45]<=2.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[14]<=3.0:
               return 'G'
            else:
               return 'G'
         elif obj[5] == 'B':
            # {"feature": "C_500600", "instances": 21, "metric_value": 8.7888, "depth": 4}
            if obj[3] == 'G':
               return 'G'
            elif obj[3] == 'B':
               # {"feature": "C_500300", "instances": 5, "metric_value": 5.2779, "depth": 5}
               if obj[2] == 'G':
                  return 'G'
               elif obj[2] == 'I':
                  return 'B'
               elif obj[2] == 'B':
                  return 'G'
               else:
                  return 'G'
            elif obj[3] == 'I':
               return 'G'
            else:
               return 'G'
         elif obj[5] == 'I':
            return 'G'
         else:
            return 'G'
      elif obj[1] == '10101':
         # {"feature": "C_100110", "instances": 170, "metric_value": 21.9576, "depth": 3}
         if obj[13]<=2.0:
            # {"feature": "C_100000", "instances": 104, "metric_value": 15.5707, "depth": 4}
            if obj[18]>5.0:
               # {"feature": "C_106880", "instances": 65, "metric_value": 10.6772, "depth": 5}
               if obj[10]<=3.0:
                  return 'G'
               elif obj[10]>3.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[18]<=5.0:
               # {"feature": "C_990660", "instances": 39, "metric_value": 11.8635, "depth": 5}
               if obj[46]>-10.129999999999999:
                  return 'G'
               elif obj[46]<=-10.129999999999999:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[13]>2.0:
            # {"feature": "C_502400", "instances": 66, "metric_value": 16.1658, "depth": 4}
            if obj[5] == 'G':
               return 'G'
            elif obj[5] == 'I':
               # {"feature": "C_500300", "instances": 6, "metric_value": 4.5765, "depth": 5}
               if obj[2] == 'G':
                  return 'G'
               elif obj[2] == 'I':
                  return 'B'
               else:
                  return 'G'
            elif obj[5] == 'B':
               return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '11111':
         # {"feature": "C_502400", "instances": 48, "metric_value": 15.4362, "depth": 3}
         if obj[5] == 'G':
            # {"feature": "C_107480", "instances": 32, "metric_value": 10.6248, "depth": 4}
            if obj[31]<=72.39375000000001:
               # {"feature": "C_106880", "instances": 18, "metric_value": 7.5793, "depth": 5}
               if obj[10]<=5.0:
                  return 'G'
               elif obj[10]>5.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[31]>72.39375000000001:
               return 'G'
            else:
               return 'G'
         elif obj[5] == 'B':
            return 'G'
         elif obj[5] == 'I':
            return 'G'
         else:
            return 'G'
      elif obj[1] == '11110':
         # {"feature": "C_100120", "instances": 28, "metric_value": 8.7651, "depth": 3}
         if obj[14]<=11.0:
            # {"feature": "C_502400", "instances": 23, "metric_value": 9.9028, "depth": 4}
            if obj[5] == 'G':
               # {"feature": "C_106860", "instances": 15, "metric_value": 6.7639, "depth": 5}
               if obj[9]<=2.0:
                  return 'G'
               elif obj[9]>2.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[5] == 'B':
               return 'G'
            elif obj[5] == 'I':
               return 'B'
            else:
               return 'G'
         elif obj[14]>11.0:
            return 'B'
         else:
            return 'G'
      elif obj[1] == '11101':
         return 'G'
      else:
         return 'G'
   elif obj[0] == '00011':
      # {"feature": "C_660570", "instances": 11799, "metric_value": 311.9135, "depth": 2}
      if obj[1] == '00011':
         # {"feature": "C_912070", "instances": 5163, "metric_value": 131.5606, "depth": 3}
         if obj[34]>0.0:
            # {"feature": "C_114100", "instances": 2825, "metric_value": 93.9429, "depth": 4}
            if obj[41]>0.5596986194690265:
               # {"feature": "C_106820", "instances": 1578, "metric_value": 65.8609, "depth": 5}
               if obj[30]<=0.0:
                  return 'G'
               elif obj[30]>0.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[41]<=0.5596986194690265:
               # {"feature": "C_106820", "instances": 1247, "metric_value": 66.9999, "depth": 5}
               if obj[30]>0.0:
                  return 'G'
               elif obj[30]<=0.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[34]<=0.0:
            # {"feature": "C_104320", "instances": 2338, "metric_value": 92.3585, "depth": 4}
            if obj[17]<=132.3977758768178:
               # {"feature": "C_100000", "instances": 1270, "metric_value": 66.158, "depth": 5}
               if obj[18]<=1.0:
                  return 'G'
               elif obj[18]>1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[17]>132.3977758768178:
               # {"feature": "C_107480", "instances": 1068, "metric_value": 64.5033, "depth": 5}
               if obj[31]<=193.97921348314608:
                  return 'G'
               elif obj[31]>193.97921348314608:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '10011':
         # {"feature": "C_502400", "instances": 4998, "metric_value": 133.5862, "depth": 3}
         if obj[5] == 'G':
            # {"feature": "C_961223", "instances": 3859, "metric_value": 118.5771, "depth": 4}
            if obj[43]<=-434.5072220782586:
               # {"feature": "C_116000", "instances": 1942, "metric_value": 83.6557, "depth": 5}
               if obj[45]>0.0:
                  return 'G'
               elif obj[45]<=0.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[43]>-434.5072220782586:
               # {"feature": "C_100120", "instances": 1917, "metric_value": 84.0959, "depth": 5}
               if obj[14]>1.0:
                  return 'G'
               elif obj[14]<=1.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[5] == 'B':
            # {"feature": "C_501200", "instances": 745, "metric_value": 47.4877, "depth": 4}
            if obj[4] == 'B':
               # {"feature": "C_500600", "instances": 426, "metric_value": 35.1661, "depth": 5}
               if obj[3] == 'B':
                  return 'G'
               elif obj[3] == 'G':
                  return 'G'
               elif obj[3] == 'I':
                  return 'G'
               else:
                  return 'G'
            elif obj[4] == 'G':
               # {"feature": "C_600160", "instances": 283, "metric_value": 28.4634, "depth": 5}
               if obj[42]<=26.992932862190813:
                  return 'G'
               elif obj[42]>26.992932862190813:
                  return 'G'
               else:
                  return 'G'
            elif obj[4] == 'I':
               # {"feature": "C_107480", "instances": 30, "metric_value": 7.3452, "depth": 5}
               if obj[31]>26.90795710995214:
                  return 'G'
               elif obj[31]<=26.90795710995214:
                  return 'B'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[5] == 'I':
            # {"feature": "C_116000", "instances": 378, "metric_value": 27.2521, "depth": 4}
            if obj[45]>0.0:
               # {"feature": "C_100140", "instances": 304, "metric_value": 21.802, "depth": 5}
               if obj[15]>1.0:
                  return 'G'
               elif obj[15]<=1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[45]<=0.0:
               return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '10111':
         # {"feature": "C_502400", "instances": 418, "metric_value": 39.9282, "depth": 3}
         if obj[5] == 'G':
            # {"feature": "C_104320", "instances": 319, "metric_value": 34.1589, "depth": 4}
            if obj[17]<=156.92163009404388:
               # {"feature": "C_110720", "instances": 164, "metric_value": 24.0743, "depth": 5}
               if obj[32]<=0.0:
                  return 'G'
               elif obj[32]>0.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[17]>156.92163009404388:
               # {"feature": "C_999032", "instances": 155, "metric_value": 24.2622, "depth": 5}
               if obj[35]<=0.0:
                  return 'G'
               elif obj[35]>0.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[5] == 'B':
            # {"feature": "C_501200", "instances": 69, "metric_value": 15.1699, "depth": 4}
            if obj[4] == 'B':
               # {"feature": "C_500600", "instances": 38, "metric_value": 13.145, "depth": 5}
               if obj[3] == 'B':
                  return 'G'
               elif obj[3] == 'G':
                  return 'G'
               elif obj[3] == 'I':
                  return 'G'
               else:
                  return 'G'
            elif obj[4] == 'G':
               # {"feature": "C_111300", "instances": 27, "metric_value": 8.4312, "depth": 5}
               if obj[38]<=32.0:
                  return 'G'
               elif obj[38]>32.0:
                  return 'B'
               else:
                  return 'G'
            elif obj[4] == 'I':
               return 'G'
            else:
               return 'G'
         elif obj[5] == 'I':
            # {"feature": "C_906170", "instances": 28, "metric_value": 9.1494, "depth": 4}
            if obj[26]>0.0:
               # {"feature": "C_106880", "instances": 17, "metric_value": 6.4489, "depth": 5}
               if obj[10]<=4.0:
                  return 'G'
               elif obj[10]>4.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[26]<=0.0:
               return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '01011':
         # {"feature": "C_107480", "instances": 397, "metric_value": 38.834, "depth": 3}
         if obj[31]>189.58765743073045:
            # {"feature": "C_999032", "instances": 215, "metric_value": 28.2224, "depth": 4}
            if obj[35]<=0.0:
               # {"feature": "C_930623", "instances": 118, "metric_value": 20.6231, "depth": 5}
               if obj[27]<=-1000.0:
                  return 'G'
               elif obj[27]>-1000.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[35]>0.0:
               # {"feature": "C_110720", "instances": 97, "metric_value": 19.2879, "depth": 5}
               if obj[32]<=7.0:
                  return 'G'
               elif obj[32]>7.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[31]<=189.58765743073045:
            # {"feature": "C_990660", "instances": 182, "metric_value": 26.6829, "depth": 4}
            if obj[46]<=-470.75560439560434:
               return 'G'
            elif obj[46]>-470.75560439560434:
               # {"feature": "C_100140", "instances": 90, "metric_value": 18.5461, "depth": 5}
               if obj[15]<=2.0:
                  return 'G'
               elif obj[15]>2.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '11011':
         # {"feature": "C_100000", "instances": 373, "metric_value": 37.8, "depth": 3}
         if obj[18]>5.0:
            # {"feature": "C_502400", "instances": 191, "metric_value": 26.7877, "depth": 4}
            if obj[5] == 'G':
               # {"feature": "C_110720", "instances": 167, "metric_value": 25.2335, "depth": 5}
               if obj[32]<=5.664670658682635:
                  return 'G'
               elif obj[32]>5.664670658682635:
                  return 'G'
               else:
                  return 'G'
            elif obj[5] == 'B':
               # {"feature": "C_501200", "instances": 16, "metric_value": 8.0868, "depth": 5}
               if obj[4] == 'G':
                  return 'G'
               elif obj[4] == 'B':
                  return 'G'
               elif obj[4] == 'I':
                  return 'G'
               else:
                  return 'G'
            elif obj[5] == 'I':
               return 'G'
            else:
               return 'G'
         elif obj[18]<=5.0:
            # {"feature": "C_600160", "instances": 182, "metric_value": 26.685, "depth": 4}
            if obj[42]>24.928571428571427:
               return 'G'
            elif obj[42]<=24.928571428571427:
               # {"feature": "C_502400", "instances": 91, "metric_value": 18.9437, "depth": 5}
               if obj[5] == 'G':
                  return 'G'
               elif obj[5] == 'B':
                  return 'G'
               elif obj[5] == 'I':
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '00111':
         # {"feature": "C_930623", "instances": 314, "metric_value": 33.6424, "depth": 3}
         if obj[27]>-72.18955414012736:
            # {"feature": "C_100000", "instances": 161, "metric_value": 23.4917, "depth": 4}
            if obj[18]<=3.0:
               # {"feature": "C_107480", "instances": 83, "metric_value": 16.4805, "depth": 5}
               if obj[31]<=131.36385542168676:
                  return 'G'
               elif obj[31]>131.36385542168676:
                  return 'G'
               else:
                  return 'G'
            elif obj[18]>3.0:
               # {"feature": "C_106880", "instances": 78, "metric_value": 16.7776, "depth": 5}
               if obj[10]<=1.0:
                  return 'G'
               elif obj[10]>1.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[27]<=-72.18955414012736:
            # {"feature": "C_100140", "instances": 153, "metric_value": 24.0906, "depth": 4}
            if obj[15]>1.0:
               # {"feature": "C_106880", "instances": 78, "metric_value": 17.2149, "depth": 5}
               if obj[10]<=1.0:
                  return 'G'
               elif obj[10]>1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[15]<=1.0:
               # {"feature": "C_107480", "instances": 75, "metric_value": 16.8637, "depth": 5}
               if obj[31]<=89.17733333333334:
                  return 'G'
               elif obj[31]>89.17733333333334:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '11111':
         return 'G'
      elif obj[1] == '01111':
         return 'G'
      else:
         return 'G'
   elif obj[0] == '10111':
      # {"feature": "C_912070", "instances": 10706, "metric_value": 160.7202, "depth": 2}
      if obj[34]>0.0:
         # {"feature": "C_107480", "instances": 6136, "metric_value": 109.6373, "depth": 3}
         if obj[31]<=42.18474576271186:
            # {"feature": "C_750100", "instances": 3694, "metric_value": 77.4632, "depth": 4}
            if obj[19]<=2.0:
               # {"feature": "C_502400", "instances": 3404, "metric_value": 87.4458, "depth": 5}
               if obj[5] == 'G':
                  return 'G'
               elif obj[5] == 'I':
                  return 'G'
               elif obj[5] == 'B':
                  return 'G'
               else:
                  return 'G'
            elif obj[19]>2.0:
               # {"feature": "C_111780", "instances": 290, "metric_value": 24.6568, "depth": 5}
               if obj[39]<=0.0:
                  return 'B'
               elif obj[39]>0.0:
                  return 'B'
               else:
                  return 'B'
            else:
               return 'G'
         elif obj[31]>42.18474576271186:
            # {"feature": "C_502400", "instances": 2442, "metric_value": 80.7345, "depth": 4}
            if obj[5] == 'G':
               # {"feature": "C_100110", "instances": 1789, "metric_value": 77.7859, "depth": 5}
               if obj[13]>1.0:
                  return 'G'
               elif obj[13]<=1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[5] == 'I':
               # {"feature": "C_750100", "instances": 356, "metric_value": 25.3476, "depth": 5}
               if obj[19]<=3.0:
                  return 'G'
               elif obj[19]>3.0:
                  return 'B'
               else:
                  return 'G'
            elif obj[5] == 'B':
               # {"feature": "C_500300", "instances": 297, "metric_value": 26.188, "depth": 5}
               if obj[2] == 'G':
                  return 'G'
               elif obj[2] == 'I':
                  return 'B'
               elif obj[2] == 'B':
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[34]<=0.0:
         # {"feature": "C_114100", "instances": 4570, "metric_value": 118.635, "depth": 3}
         if obj[41]>0.6540219693654267:
            # {"feature": "C_100110", "instances": 2386, "metric_value": 82.828, "depth": 4}
            if obj[13]>1.0:
               # {"feature": "C_502400", "instances": 1278, "metric_value": 62.4217, "depth": 5}
               if obj[5] == 'G':
                  return 'G'
               elif obj[5] == 'B':
                  return 'G'
               elif obj[5] == 'I':
                  return 'G'
               else:
                  return 'G'
            elif obj[13]<=1.0:
               # {"feature": "C_116000", "instances": 1108, "metric_value": 55.102, "depth": 5}
               if obj[45]>3.0:
                  return 'G'
               elif obj[45]<=3.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[41]<=0.6540219693654267:
            # {"feature": "C_502400", "instances": 2184, "metric_value": 85.4521, "depth": 4}
            if obj[5] == 'G':
               # {"feature": "C_100110", "instances": 1754, "metric_value": 78.7971, "depth": 5}
               if obj[13]<=1.0:
                  return 'G'
               elif obj[13]>1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[5] == 'B':
               # {"feature": "C_501200", "instances": 331, "metric_value": 32.5841, "depth": 5}
               if obj[4] == 'G':
                  return 'G'
               elif obj[4] == 'B':
                  return 'G'
               elif obj[4] == 'I':
                  return 'G'
               else:
                  return 'G'
            elif obj[5] == 'I':
               # {"feature": "C_750100", "instances": 99, "metric_value": 14.0876, "depth": 5}
               if obj[19]<=2.0:
                  return 'G'
               elif obj[19]>2.0:
                  return 'B'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      else:
         return 'G'
   elif obj[0] == '01010':
      # {"feature": "C_660570", "instances": 10372, "metric_value": 327.6716, "depth": 2}
      if obj[1] == '01010':
         # {"feature": "C_111640", "instances": 4781, "metric_value": 135.4774, "depth": 3}
         if obj[7]>-1.0:
            # {"feature": "C_110720", "instances": 2450, "metric_value": 95.1211, "depth": 4}
            if obj[32]<=6.686938775510204:
               # {"feature": "C_100000", "instances": 1304, "metric_value": 68.2142, "depth": 5}
               if obj[18]<=2.0:
                  return 'G'
               elif obj[18]>2.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[32]>6.686938775510204:
               # {"feature": "C_100000", "instances": 1146, "metric_value": 66.2657, "depth": 5}
               if obj[18]>2.0:
                  return 'G'
               elif obj[18]<=2.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[7]<=-1.0:
            # {"feature": "C_104320", "instances": 2331, "metric_value": 96.4097, "depth": 4}
            if obj[17]>156.82754182754184:
               return 'G'
            elif obj[17]<=156.82754182754184:
               # {"feature": "C_114900", "instances": 1080, "metric_value": 65.5723, "depth": 5}
               if obj[49]<=367.06388888888887:
                  return 'G'
               elif obj[49]>367.06388888888887:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '11010':
         # {"feature": "C_750600", "instances": 3178, "metric_value": 108.9935, "depth": 3}
         if obj[21]>1.0:
            # {"feature": "C_100120", "instances": 1613, "metric_value": 76.7249, "depth": 4}
            if obj[14]<=1.0:
               # {"feature": "C_100000", "instances": 863, "metric_value": 55.4902, "depth": 5}
               if obj[18]>3.0:
                  return 'G'
               elif obj[18]<=3.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[14]>1.0:
               # {"feature": "C_104320", "instances": 750, "metric_value": 52.9503, "depth": 5}
               if obj[17]>165.524:
                  return 'G'
               elif obj[17]<=165.524:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[21]<=1.0:
            # {"feature": "C_104320", "instances": 1565, "metric_value": 77.4085, "depth": 4}
            if obj[17]>153.09137380191694:
               # {"feature": "C_600160", "instances": 806, "metric_value": 54.811, "depth": 5}
               if obj[42]>28.496277915632753:
                  return 'G'
               elif obj[42]<=28.496277915632753:
                  return 'G'
               else:
                  return 'G'
            elif obj[17]<=153.09137380191694:
               # {"feature": "C_650640", "instances": 759, "metric_value": 54.6631, "depth": 5}
               if obj[25]>2179.0434782608695:
                  return 'G'
               elif obj[25]<=2179.0434782608695:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '01110':
         # {"feature": "C_100000", "instances": 720, "metric_value": 51.4341, "depth": 3}
         if obj[18]>3.0:
            # {"feature": "C_111600", "instances": 370, "metric_value": 36.4016, "depth": 4}
            if obj[48]>-1.0:
               # {"feature": "C_650640", "instances": 202, "metric_value": 26.2072, "depth": 5}
               if obj[25]<=7581.658415841584:
                  return 'G'
               elif obj[25]>7581.658415841584:
                  return 'G'
               else:
                  return 'G'
            elif obj[48]<=-1.0:
               # {"feature": "C_110720", "instances": 168, "metric_value": 25.3053, "depth": 5}
               if obj[32]<=6.0:
                  return 'G'
               elif obj[32]>6.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[18]<=3.0:
            # {"feature": "C_110720", "instances": 350, "metric_value": 36.3479, "depth": 4}
            if obj[32]<=6.582857142857143:
               # {"feature": "C_107480", "instances": 178, "metric_value": 25.7976, "depth": 5}
               if obj[31]<=98.988202247191:
                  return 'G'
               elif obj[31]>98.988202247191:
                  return 'G'
               else:
                  return 'G'
            elif obj[32]>6.582857142857143:
               # {"feature": "C_751200", "instances": 172, "metric_value": 25.6079, "depth": 5}
               if obj[22]>1.0:
                  return 'G'
               elif obj[22]<=1.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '11011':
         # {"feature": "C_100120", "instances": 513, "metric_value": 44.0626, "depth": 3}
         if obj[14]>1.0:
            # {"feature": "C_750100", "instances": 257, "metric_value": 31.3141, "depth": 4}
            if obj[19]<=1.0:
               # {"feature": "C_100000", "instances": 132, "metric_value": 22.2812, "depth": 5}
               if obj[18]<=6.0:
                  return 'G'
               elif obj[18]>6.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[19]>1.0:
               # {"feature": "C_102800", "instances": 125, "metric_value": 22.0054, "depth": 5}
               if obj[28]>15.38:
                  return 'G'
               elif obj[28]<=15.38:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[14]<=1.0:
            # {"feature": "C_107480", "instances": 256, "metric_value": 31.0143, "depth": 4}
            if obj[31]<=93.491796875:
               # {"feature": "C_111640", "instances": 135, "metric_value": 21.8916, "depth": 5}
               if obj[7]>-1.0:
                  return 'G'
               elif obj[7]<=-1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[31]>93.491796875:
               return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '11110':
         # {"feature": "C_750100", "instances": 513, "metric_value": 44.5891, "depth": 3}
         if obj[19]>1.0:
            # {"feature": "C_100120", "instances": 274, "metric_value": 32.1333, "depth": 4}
            if obj[14]>1.0:
               # {"feature": "C_104320", "instances": 142, "metric_value": 23.1522, "depth": 5}
               if obj[17]>162.26760563380282:
                  return 'G'
               elif obj[17]<=162.26760563380282:
                  return 'G'
               else:
                  return 'G'
            elif obj[14]<=1.0:
               # {"feature": "C_100000", "instances": 132, "metric_value": 22.2837, "depth": 5}
               if obj[18]>4.0:
                  return 'G'
               elif obj[18]<=4.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[19]<=1.0:
            return 'G'
         else:
            return 'G'
      elif obj[1] == '01011':
         # {"feature": "C_102800", "instances": 459, "metric_value": 40.1253, "depth": 3}
         if obj[28]>30.0:
            # {"feature": "C_105740", "instances": 255, "metric_value": 28.2612, "depth": 4}
            if obj[44]<=107.15686274509804:
               # {"feature": "C_111640", "instances": 149, "metric_value": 20.2704, "depth": 5}
               if obj[7]>-1.0:
                  return 'G'
               elif obj[7]<=-1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[44]>107.15686274509804:
               # {"feature": "C_110720", "instances": 106, "metric_value": 19.8273, "depth": 5}
               if obj[32]>5.0:
                  return 'G'
               elif obj[32]<=5.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[28]<=30.0:
            return 'G'
         else:
            return 'G'
      elif obj[1] == '11111':
         # {"feature": "C_110720", "instances": 110, "metric_value": 19.8349, "depth": 3}
         if obj[32]<=8.0:
            # {"feature": "C_906370", "instances": 57, "metric_value": 14.0711, "depth": 4}
            if obj[33]>6.0:
               # {"feature": "C_104320", "instances": 32, "metric_value": 9.9657, "depth": 5}
               if obj[17]>165.84375:
                  return 'G'
               elif obj[17]<=165.84375:
                  return 'G'
               else:
                  return 'G'
            elif obj[33]<=6.0:
               return 'G'
            else:
               return 'G'
         elif obj[32]>8.0:
            # {"feature": "C_600160", "instances": 53, "metric_value": 14.0199, "depth": 4}
            if obj[42]>33.056603773584904:
               # {"feature": "C_103380", "instances": 28, "metric_value": 9.8487, "depth": 5}
               if obj[36]>14.29:
                  return 'G'
               elif obj[36]<=14.29:
                  return 'G'
               else:
                  return 'G'
            elif obj[42]<=33.056603773584904:
               return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '01111':
         # {"feature": "C_100140", "instances": 98, "metric_value": 18.9989, "depth": 3}
         if obj[15]<=2.0:
            # {"feature": "C_111620", "instances": 55, "metric_value": 13.7764, "depth": 4}
            if obj[6]>-1.0:
               # {"feature": "C_501200", "instances": 29, "metric_value": 9.5159, "depth": 5}
               if obj[4] == 'G':
                  return 'G'
               elif obj[4] == 'B':
                  return 'G'
               elif obj[4] == 'I':
                  return 'G'
               else:
                  return 'G'
            elif obj[6]<=-1.0:
               return 'G'
            else:
               return 'G'
         elif obj[15]>2.0:
            return 'G'
         else:
            return 'G'
      else:
         return 'G'
   elif obj[0] == '11111':
      # {"feature": "C_114100", "instances": 9493, "metric_value": 172.0133, "depth": 2}
      if obj[41]>0.7144802064679238:
         # {"feature": "C_100110", "instances": 5166, "metric_value": 124.6613, "depth": 3}
         if obj[13]>1.0:
            # {"feature": "C_116000", "instances": 2726, "metric_value": 90.8127, "depth": 4}
            if obj[45]>5.0:
               # {"feature": "C_106600", "instances": 1443, "metric_value": 64.5152, "depth": 5}
               if obj[37]>1.0:
                  return 'G'
               elif obj[37]<=1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[45]<=5.0:
               # {"feature": "C_906370", "instances": 1283, "metric_value": 63.944, "depth": 5}
               if obj[33]>17.104442712392828:
                  return 'G'
               elif obj[33]<=17.104442712392828:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[13]<=1.0:
            # {"feature": "C_104320", "instances": 2440, "metric_value": 85.5095, "depth": 4}
            if obj[17]>146.4487704918033:
               # {"feature": "C_912070", "instances": 1342, "metric_value": 62.0805, "depth": 5}
               if obj[34]>0.0:
                  return 'G'
               elif obj[34]<=0.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[17]<=146.4487704918033:
               # {"feature": "C_116000", "instances": 1098, "metric_value": 58.9451, "depth": 5}
               if obj[45]>4.0:
                  return 'G'
               elif obj[45]<=4.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[41]<=0.7144802064679238:
         # {"feature": "C_990370", "instances": 4327, "metric_value": 118.5969, "depth": 3}
         if obj[40]>-468.3473122255605:
            # {"feature": "C_906170", "instances": 2213, "metric_value": 81.3771, "depth": 4}
            if obj[26]>1.0:
               # {"feature": "C_912070", "instances": 1315, "metric_value": 59.2917, "depth": 5}
               if obj[34]>3.0:
                  return 'G'
               elif obj[34]<=3.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[26]<=1.0:
               # {"feature": "C_912070", "instances": 898, "metric_value": 55.8216, "depth": 5}
               if obj[34]>0.0:
                  return 'G'
               elif obj[34]<=0.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[40]<=-468.3473122255605:
            # {"feature": "C_107480", "instances": 2114, "metric_value": 86.3829, "depth": 4}
            if obj[31]<=84.92890255439923:
               # {"feature": "C_104320", "instances": 1157, "metric_value": 63.9141, "depth": 5}
               if obj[17]>198.49697493517718:
                  return 'G'
               elif obj[17]<=198.49697493517718:
                  return 'G'
               else:
                  return 'G'
            elif obj[31]>84.92890255439923:
               # {"feature": "C_104320", "instances": 957, "metric_value": 58.2713, "depth": 5}
               if obj[17]<=251.44723092998956:
                  return 'G'
               elif obj[17]>251.44723092998956:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      else:
         return 'G'
   elif obj[0] == '01011':
      # {"feature": "C_660570", "instances": 8662, "metric_value": 228.9865, "depth": 2}
      if obj[1] == '11011':
         # {"feature": "C_106880", "instances": 3794, "metric_value": 115.8555, "depth": 3}
         if obj[10]>1.0:
            # {"feature": "C_104320", "instances": 1913, "metric_value": 81.6222, "depth": 4}
            if obj[17]>191.39571353894408:
               # {"feature": "C_100000", "instances": 1057, "metric_value": 59.2651, "depth": 5}
               if obj[18]>6.0:
                  return 'G'
               elif obj[18]<=6.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[17]<=191.39571353894408:
               # {"feature": "C_103380", "instances": 856, "metric_value": 56.1921, "depth": 5}
               if obj[36]>0.0:
                  return 'G'
               elif obj[36]<=0.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[10]<=1.0:
            # {"feature": "C_107480", "instances": 1881, "metric_value": 82.2283, "depth": 4}
            if obj[31]>110.55629984051038:
               # {"feature": "C_100000", "instances": 956, "metric_value": 57.8418, "depth": 5}
               if obj[18]<=4.0:
                  return 'G'
               elif obj[18]>4.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[31]<=110.55629984051038:
               # {"feature": "C_100000", "instances": 925, "metric_value": 58.4695, "depth": 5}
               if obj[18]>4.0:
                  return 'G'
               elif obj[18]<=4.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '01011':
         # {"feature": "C_100000", "instances": 3678, "metric_value": 114.6627, "depth": 3}
         if obj[18]<=3.0:
            # {"feature": "C_100140", "instances": 1914, "metric_value": 83.0947, "depth": 4}
            if obj[15]>1.0:
               # {"feature": "C_650640", "instances": 1007, "metric_value": 59.9484, "depth": 5}
               if obj[25]<=3579.5849056603774:
                  return 'G'
               elif obj[25]>3579.5849056603774:
                  return 'G'
               else:
                  return 'G'
            elif obj[15]<=1.0:
               # {"feature": "C_107480", "instances": 907, "metric_value": 57.5641, "depth": 5}
               if obj[31]>126.90066152149944:
                  return 'G'
               elif obj[31]<=126.90066152149944:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[18]>3.0:
            # {"feature": "C_107480", "instances": 1764, "metric_value": 79.0459, "depth": 4}
            if obj[31]>143.46201814058955:
               # {"feature": "C_906370", "instances": 945, "metric_value": 56.9638, "depth": 5}
               if obj[33]>4.861375661375662:
                  return 'G'
               elif obj[33]<=4.861375661375662:
                  return 'G'
               else:
                  return 'G'
            elif obj[31]<=143.46201814058955:
               # {"feature": "C_110720", "instances": 819, "metric_value": 54.8633, "depth": 5}
               if obj[32]<=5.968253968253968:
                  return 'G'
               elif obj[32]>5.968253968253968:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '11111':
         # {"feature": "C_100100", "instances": 642, "metric_value": 47.8473, "depth": 3}
         if obj[12]<=1.0:
            # {"feature": "C_114100", "instances": 335, "metric_value": 33.7879, "depth": 4}
            if obj[41]>0.6713588059701492:
               # {"feature": "C_906370", "instances": 175, "metric_value": 23.4777, "depth": 5}
               if obj[33]<=6.0:
                  return 'G'
               elif obj[33]>6.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[41]<=0.6713588059701492:
               # {"feature": "C_107480", "instances": 160, "metric_value": 24.3495, "depth": 5}
               if obj[31]>112.60125000000001:
                  return 'G'
               elif obj[31]<=112.60125000000001:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[12]>1.0:
            # {"feature": "C_502400", "instances": 307, "metric_value": 35.2226, "depth": 4}
            if obj[5] == 'G':
               # {"feature": "C_100120", "instances": 260, "metric_value": 31.2588, "depth": 5}
               if obj[14]<=1.0:
                  return 'G'
               elif obj[14]>1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[5] == 'B':
               return 'G'
            elif obj[5] == 'I':
               # {"feature": "C_501200", "instances": 23, "metric_value": 8.7867, "depth": 5}
               if obj[4] == 'I':
                  return 'G'
               elif obj[4] == 'G':
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '01111':
         # {"feature": "C_100100", "instances": 548, "metric_value": 45.4318, "depth": 3}
         if obj[12]<=1.0:
            # {"feature": "C_906370", "instances": 304, "metric_value": 33.2816, "depth": 4}
            if obj[33]>0.0:
               # {"feature": "C_104320", "instances": 162, "metric_value": 23.5957, "depth": 5}
               if obj[17]>187.93827160493828:
                  return 'G'
               elif obj[17]<=187.93827160493828:
                  return 'G'
               else:
                  return 'G'
            elif obj[33]<=0.0:
               # {"feature": "C_114900", "instances": 142, "metric_value": 23.4941, "depth": 5}
               if obj[49]>331.6478873239437:
                  return 'G'
               elif obj[49]<=331.6478873239437:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[12]>1.0:
            # {"feature": "C_107480", "instances": 244, "metric_value": 30.9761, "depth": 4}
            if obj[31]>133.98360655737704:
               # {"feature": "C_102800", "instances": 130, "metric_value": 22.4553, "depth": 5}
               if obj[28]<=36.36:
                  return 'G'
               elif obj[28]>36.36:
                  return 'G'
               else:
                  return 'G'
            elif obj[31]<=133.98360655737704:
               return 'G'
            else:
               return 'G'
         else:
            return 'G'
      else:
         return 'G'
   elif obj[0] == '00100':
      # {"feature": "C_660570", "instances": 7788, "metric_value": 295.6705, "depth": 2}
      if obj[1] == '00100':
         # {"feature": "C_114900", "instances": 3735, "metric_value": 116.8065, "depth": 3}
         if obj[49]>58.55689424364123:
            # {"feature": "C_107480", "instances": 1964, "metric_value": 83.3308, "depth": 4}
            if obj[31]<=24.178360488798372:
               # {"feature": "C_751200", "instances": 1072, "metric_value": 61.3081, "depth": 5}
               if obj[22]>0.0:
                  return 'G'
               elif obj[22]<=0.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[31]>24.178360488798372:
               # {"feature": "C_114100", "instances": 892, "metric_value": 56.5184, "depth": 5}
               if obj[41]<=0.6044751121076234:
                  return 'G'
               elif obj[41]>0.6044751121076234:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[49]<=58.55689424364123:
            # {"feature": "C_906370", "instances": 1771, "metric_value": 81.7901, "depth": 4}
            if obj[33]>5.0:
               # {"feature": "C_114100", "instances": 887, "metric_value": 57.6056, "depth": 5}
               if obj[41]<=0.8797922209695603:
                  return 'G'
               elif obj[41]>0.8797922209695603:
                  return 'G'
               else:
                  return 'G'
            elif obj[33]<=5.0:
               # {"feature": "C_107480", "instances": 884, "metric_value": 57.7127, "depth": 5}
               if obj[31]<=23.098190045248867:
                  return 'G'
               elif obj[31]>23.098190045248867:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '10100':
         # {"feature": "C_107480", "instances": 2392, "metric_value": 86.2647, "depth": 3}
         if obj[31]<=37.03064381270903:
            # {"feature": "C_600160", "instances": 1341, "metric_value": 63.0831, "depth": 4}
            if obj[42]<=22.839671886651754:
               # {"feature": "C_104320", "instances": 674, "metric_value": 44.1451, "depth": 5}
               if obj[17]<=35.4213649851632:
                  return 'G'
               elif obj[17]>35.4213649851632:
                  return 'G'
               else:
                  return 'G'
            elif obj[42]>22.839671886651754:
               # {"feature": "C_104320", "instances": 667, "metric_value": 45.1153, "depth": 5}
               if obj[17]>48.892053973013496:
                  return 'G'
               elif obj[17]<=48.892053973013496:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[31]>37.03064381270903:
            # {"feature": "C_502400", "instances": 1051, "metric_value": 60.7154, "depth": 4}
            if obj[5] == 'G':
               # {"feature": "C_106880", "instances": 801, "metric_value": 55.1889, "depth": 5}
               if obj[10]<=1.0:
                  return 'G'
               elif obj[10]>1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[5] == 'B':
               # {"feature": "C_501200", "instances": 165, "metric_value": 19.5498, "depth": 5}
               if obj[4] == 'B':
                  return 'G'
               elif obj[4] == 'G':
                  return 'G'
               elif obj[4] == 'I':
                  return 'G'
               else:
                  return 'G'
            elif obj[5] == 'I':
               # {"feature": "C_104320", "instances": 83, "metric_value": 13.7672, "depth": 5}
               if obj[17]<=79.59036144578313:
                  return 'G'
               elif obj[17]>79.59036144578313:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '10111':
         # {"feature": "C_502400", "instances": 538, "metric_value": 42.4177, "depth": 3}
         if obj[5] == 'G':
            # {"feature": "C_906370", "instances": 375, "metric_value": 37.0945, "depth": 4}
            if obj[33]<=5.0:
               # {"feature": "C_114100", "instances": 200, "metric_value": 26.2994, "depth": 5}
               if obj[41]<=0.590705:
                  return 'G'
               elif obj[41]>0.590705:
                  return 'G'
               else:
                  return 'G'
            elif obj[33]>5.0:
               # {"feature": "C_114100", "instances": 175, "metric_value": 26.1511, "depth": 5}
               if obj[41]<=0.8860131428571428:
                  return 'G'
               elif obj[41]>0.8860131428571428:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[5] == 'B':
            # {"feature": "C_501200", "instances": 108, "metric_value": 16.1073, "depth": 4}
            if obj[4] == 'B':
               # {"feature": "C_500600", "instances": 52, "metric_value": 10.9295, "depth": 5}
               if obj[3] == 'B':
                  return 'G'
               elif obj[3] == 'G':
                  return 'G'
               elif obj[3] == 'I':
                  return 'G'
               else:
                  return 'G'
            elif obj[4] == 'G':
               # {"feature": "C_100120", "instances": 41, "metric_value": 9.9183, "depth": 5}
               if obj[14]<=3.0:
                  return 'G'
               elif obj[14]>3.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[4] == 'I':
               # {"feature": "C_750100", "instances": 11, "metric_value": 6.2426, "depth": 5}
               if obj[19]<=2.0:
                  return 'G'
               elif obj[19]>2.0:
                  return 'B'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[5] == 'I':
            # {"feature": "C_750100", "instances": 55, "metric_value": 12.3149, "depth": 4}
            if obj[19]<=2.0:
               # {"feature": "C_600160", "instances": 48, "metric_value": 12.2045, "depth": 5}
               if obj[42]>28.708333333333332:
                  return 'G'
               elif obj[42]<=28.708333333333332:
                  return 'G'
               else:
                  return 'G'
            elif obj[19]>2.0:
               return 'B'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '00111':
         # {"feature": "C_100110", "instances": 420, "metric_value": 34.0836, "depth": 3}
         if obj[13]<=6.0:
            # {"feature": "C_105740", "instances": 368, "metric_value": 33.8493, "depth": 4}
            if obj[44]<=50.95923913043478:
               # {"feature": "C_650640", "instances": 230, "metric_value": 25.146, "depth": 5}
               if obj[25]<=1473.4782608695652:
                  return 'G'
               elif obj[25]>1473.4782608695652:
                  return 'G'
               else:
                  return 'G'
            elif obj[44]>50.95923913043478:
               # {"feature": "C_114100", "instances": 138, "metric_value": 22.8192, "depth": 5}
               if obj[41]>0.6867463768115942:
                  return 'G'
               elif obj[41]<=0.6867463768115942:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[13]>6.0:
            return 'B'
         else:
            return 'G'
      elif obj[1] == '10110':
         # {"feature": "C_502400", "instances": 162, "metric_value": 26.0066, "depth": 3}
         if obj[5] == 'G':
            # {"feature": "C_100110", "instances": 91, "metric_value": 18.6615, "depth": 4}
            if obj[13]>1.0:
               # {"feature": "C_100120", "instances": 46, "metric_value": 12.9861, "depth": 5}
               if obj[14]<=1.0:
                  return 'G'
               elif obj[14]>1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[13]<=1.0:
               return 'G'
            else:
               return 'G'
         elif obj[5] == 'B':
            # {"feature": "C_501200", "instances": 61, "metric_value": 15.5793, "depth": 4}
            if obj[4] == 'B':
               # {"feature": "C_500300", "instances": 36, "metric_value": 11.0882, "depth": 5}
               if obj[2] == 'G':
                  return 'G'
               elif obj[2] == 'B':
                  return 'G'
               elif obj[2] == 'I':
                  return 'B'
               else:
                  return 'G'
            elif obj[4] == 'G':
               # {"feature": "C_104320", "instances": 19, "metric_value": 7.8376, "depth": 5}
               if obj[17]<=100.0:
                  return 'G'
               elif obj[17]>100.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[4] == 'I':
               return 'G'
            else:
               return 'G'
         elif obj[5] == 'I':
            # {"feature": "C_111620", "instances": 10, "metric_value": 5.6569, "depth": 4}
            if obj[6]<=1.0:
               return 'G'
            elif obj[6]>1.0:
               return 'B'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '00110':
         # {"feature": "C_502400", "instances": 161, "metric_value": 26.571, "depth": 3}
         if obj[5] == 'G':
            # {"feature": "C_100110", "instances": 121, "metric_value": 21.2837, "depth": 4}
            if obj[13]<=1.0:
               # {"feature": "C_906370", "instances": 64, "metric_value": 15.0262, "depth": 5}
               if obj[33]>2.0:
                  return 'G'
               elif obj[33]<=2.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[13]>1.0:
               return 'G'
            else:
               return 'G'
         elif obj[5] == 'B':
            return 'G'
         elif obj[5] == 'I':
            return 'G'
         else:
            return 'G'
      elif obj[1] == '01100':
         # {"feature": "C_114900", "instances": 129, "metric_value": 22.3619, "depth": 3}
         if obj[49]>56.27131782945737:
            return 'G'
         elif obj[49]<=56.27131782945737:
            # {"feature": "C_104320", "instances": 64, "metric_value": 15.4972, "depth": 4}
            if obj[17]<=194.1875:
               # {"feature": "C_106880", "instances": 36, "metric_value": 11.3333, "depth": 5}
               if obj[10]<=1.0:
                  return 'G'
               elif obj[10]>1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[17]>194.1875:
               return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '11100':
         # {"feature": "C_502400", "instances": 76, "metric_value": 16.5813, "depth": 3}
         if obj[5] == 'G':
            return 'G'
         elif obj[5] == 'B':
            return 'G'
         elif obj[5] == 'I':
            # {"feature": "C_111620", "instances": 6, "metric_value": 4.8284, "depth": 4}
            if obj[6]<=0.0:
               return 'G'
            elif obj[6]>0.0:
               return 'B'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '00101':
         # {"feature": "C_106860", "instances": 63, "metric_value": 15.3776, "depth": 3}
         if obj[9]<=1.0:
            # {"feature": "C_106880", "instances": 33, "metric_value": 10.8106, "depth": 4}
            if obj[10]<=1.0:
               # {"feature": "C_104320", "instances": 18, "metric_value": 7.5793, "depth": 5}
               if obj[17]<=82.0:
                  return 'G'
               elif obj[17]>82.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[10]>1.0:
               return 'G'
            else:
               return 'G'
         elif obj[9]>1.0:
            return 'G'
         else:
            return 'G'
      elif obj[1] == '10101':
         # {"feature": "C_502400", "instances": 45, "metric_value": 12.6782, "depth": 3}
         if obj[5] == 'G':
            return 'G'
         elif obj[5] == 'B':
            # {"feature": "C_106920", "instances": 7, "metric_value": 5.1623, "depth": 4}
            if obj[11]<=1.0:
               return 'G'
            elif obj[11]>1.0:
               return 'B'
            else:
               return 'G'
         elif obj[5] == 'I':
            return 'G'
         else:
            return 'G'
      elif obj[1] == '11111':
         return 'G'
      elif obj[1] == '11110':
         return 'G'
      elif obj[1] == '01111':
         return 'G'
      elif obj[1] == '01110':
         return 'G'
      elif obj[1] == '11101':
         return 'G'
      else:
         return 'G'
   elif obj[0] == '10110':
      # {"feature": "C_660570", "instances": 6780, "metric_value": 144.0642, "depth": 2}
      if obj[1] == '10110':
         # {"feature": "C_650640", "instances": 5259, "metric_value": 118.6898, "depth": 3}
         if obj[25]<=1299.0081764594029:
            # {"feature": "C_107480", "instances": 3123, "metric_value": 83.5785, "depth": 4}
            if obj[31]<=34.477553634325965:
               # {"feature": "C_110720", "instances": 1808, "metric_value": 58.3736, "depth": 5}
               if obj[32]<=5.678650442477876:
                  return 'G'
               elif obj[32]>5.678650442477876:
                  return 'G'
               else:
                  return 'G'
            elif obj[31]>34.477553634325965:
               # {"feature": "C_999032", "instances": 1315, "metric_value": 60.0778, "depth": 5}
               if obj[35]>0.0:
                  return 'G'
               elif obj[35]<=0.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[25]>1299.0081764594029:
            # {"feature": "C_114100", "instances": 2136, "metric_value": 84.6442, "depth": 4}
            if obj[41]>0.662067275280899:
               # {"feature": "C_116000", "instances": 1113, "metric_value": 60.5233, "depth": 5}
               if obj[45]>3.0:
                  return 'G'
               elif obj[45]<=3.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[41]<=0.662067275280899:
               # {"feature": "C_106880", "instances": 1023, "metric_value": 59.215, "depth": 5}
               if obj[10]>1.0:
                  return 'G'
               elif obj[10]<=1.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '10111':
         # {"feature": "C_107480", "instances": 1231, "metric_value": 49.7324, "depth": 3}
         if obj[31]<=40.26458164094232:
            # {"feature": "C_500300", "instances": 758, "metric_value": 38.3938, "depth": 4}
            if obj[2] == 'G':
               # {"feature": "C_110720", "instances": 701, "metric_value": 40.8112, "depth": 5}
               if obj[32]<=6.5392296718972895:
                  return 'G'
               elif obj[32]>6.5392296718972895:
                  return 'G'
               else:
                  return 'G'
            elif obj[2] == 'I':
               # {"feature": "C_106880", "instances": 50, "metric_value": 11.4932, "depth": 5}
               if obj[10]>2.0:
                  return 'B'
               elif obj[10]<=2.0:
                  return 'B'
               else:
                  return 'B'
            elif obj[2] == 'B':
               # {"feature": "C_930623", "instances": 7, "metric_value": 5.1623, "depth": 5}
               if obj[27]<=-3.14:
                  return 'B'
               elif obj[27]>-3.14:
                  return 'G'
               else:
                  return 'B'
            else:
               return 'G'
         elif obj[31]>40.26458164094232:
            # {"feature": "C_116000", "instances": 473, "metric_value": 34.3607, "depth": 4}
            if obj[45]>3.0:
               # {"feature": "C_106880", "instances": 253, "metric_value": 23.7247, "depth": 5}
               if obj[10]>2.0:
                  return 'G'
               elif obj[10]<=2.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[45]<=3.0:
               # {"feature": "C_100140", "instances": 220, "metric_value": 25.2188, "depth": 5}
               if obj[15]<=2.0:
                  return 'G'
               elif obj[15]>2.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '11110':
         # {"feature": "C_106880", "instances": 238, "metric_value": 26.851, "depth": 3}
         if obj[10]>2.0:
            # {"feature": "C_100000", "instances": 145, "metric_value": 19.2037, "depth": 4}
            if obj[18]>8.0:
               # {"feature": "C_500300", "instances": 80, "metric_value": 13.431, "depth": 5}
               if obj[2] == 'G':
                  return 'G'
               elif obj[2] == 'B':
                  return 'G'
               elif obj[2] == 'I':
                  return 'B'
               else:
                  return 'G'
            elif obj[18]<=8.0:
               # {"feature": "C_650640", "instances": 65, "metric_value": 14.6841, "depth": 5}
               if obj[25]<=3541.369230769231:
                  return 'G'
               elif obj[25]>3541.369230769231:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[10]<=2.0:
            # {"feature": "C_107480", "instances": 93, "metric_value": 18.8763, "depth": 4}
            if obj[31]<=94.78817204301073:
               # {"feature": "C_906370", "instances": 49, "metric_value": 13.4387, "depth": 5}
               if obj[33]>8.0:
                  return 'G'
               elif obj[33]<=8.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[31]>94.78817204301073:
               return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '11111':
         # {"feature": "C_502400", "instances": 52, "metric_value": 14.1521, "depth": 3}
         if obj[5] == 'G':
            return 'G'
         elif obj[5] == 'B':
            # {"feature": "C_111500", "instances": 11, "metric_value": 6.2426, "depth": 4}
            if obj[24]<=5.0:
               return 'B'
            elif obj[24]>5.0:
               return 'G'
            else:
               return 'B'
         elif obj[5] == 'I':
            return 'G'
         else:
            return 'G'
      else:
         return 'G'
   elif obj[0] == '11110':
      # {"feature": "C_116000", "instances": 6136, "metric_value": 141.6976, "depth": 2}
      if obj[45]>4.0:
         # {"feature": "C_100140", "instances": 3432, "metric_value": 103.8539, "depth": 3}
         if obj[15]<=1.0:
            # {"feature": "C_110720", "instances": 1736, "metric_value": 73.411, "depth": 4}
            if obj[32]<=7.649193548387097:
               # {"feature": "C_107480", "instances": 965, "metric_value": 53.747, "depth": 5}
               if obj[31]<=54.05357512953368:
                  return 'G'
               elif obj[31]>54.05357512953368:
                  return 'G'
               else:
                  return 'G'
            elif obj[32]>7.649193548387097:
               # {"feature": "C_906370", "instances": 771, "metric_value": 50.0469, "depth": 5}
               if obj[33]<=18.595330739299612:
                  return 'G'
               elif obj[33]>18.595330739299612:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[15]>1.0:
            # {"feature": "C_106860", "instances": 1696, "metric_value": 73.4682, "depth": 4}
            if obj[9]>4.0:
               # {"feature": "C_103380", "instances": 894, "metric_value": 51.6404, "depth": 5}
               if obj[36]<=5.828243847874721:
                  return 'G'
               elif obj[36]>5.828243847874721:
                  return 'G'
               else:
                  return 'G'
            elif obj[9]<=4.0:
               # {"feature": "C_106880", "instances": 802, "metric_value": 52.2779, "depth": 5}
               if obj[10]<=2.0:
                  return 'G'
               elif obj[10]>2.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[45]<=4.0:
         # {"feature": "C_106860", "instances": 2704, "metric_value": 96.5678, "depth": 3}
         if obj[9]>3.0:
            # {"feature": "C_100110", "instances": 1431, "metric_value": 68.6197, "depth": 4}
            if obj[13]<=1.0:
               # {"feature": "C_752400", "instances": 753, "metric_value": 48.0735, "depth": 5}
               if obj[23]>1.0:
                  return 'G'
               elif obj[23]<=1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[13]>1.0:
               # {"feature": "C_106880", "instances": 678, "metric_value": 49.1596, "depth": 5}
               if obj[10]>2.0:
                  return 'G'
               elif obj[10]<=2.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[9]<=3.0:
            # {"feature": "C_100000", "instances": 1273, "metric_value": 67.9957, "depth": 4}
            if obj[18]<=6.0:
               # {"feature": "C_600160", "instances": 638, "metric_value": 47.6645, "depth": 5}
               if obj[42]>-1.0:
                  return 'G'
               elif obj[42]<=-1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[18]>6.0:
               # {"feature": "C_100120", "instances": 635, "metric_value": 48.4912, "depth": 5}
               if obj[14]>3.0:
                  return 'G'
               elif obj[14]<=3.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      else:
         return 'G'
   elif obj[0] == '11100':
      # {"feature": "C_660570", "instances": 5138, "metric_value": 152.284, "depth": 2}
      if obj[1] == '11100':
         # {"feature": "C_116000", "instances": 3757, "metric_value": 110.7966, "depth": 3}
         if obj[45]>3.0:
            # {"feature": "C_104320", "instances": 1927, "metric_value": 77.8592, "depth": 4}
            if obj[17]>136.59522573949144:
               # {"feature": "C_114100", "instances": 1047, "metric_value": 54.872, "depth": 5}
               if obj[41]>0.6434441260744985:
                  return 'G'
               elif obj[41]<=0.6434441260744985:
                  return 'G'
               else:
                  return 'G'
            elif obj[17]<=136.59522573949144:
               # {"feature": "C_906370", "instances": 880, "metric_value": 55.2794, "depth": 5}
               if obj[33]>17.661363636363635:
                  return 'G'
               elif obj[33]<=17.661363636363635:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[45]<=3.0:
            # {"feature": "C_600160", "instances": 1830, "metric_value": 78.8642, "depth": 4}
            if obj[42]>23.51530054644809:
               # {"feature": "C_104320", "instances": 1012, "metric_value": 58.0084, "depth": 5}
               if obj[17]>132.4822134387352:
                  return 'G'
               elif obj[17]<=132.4822134387352:
                  return 'G'
               else:
                  return 'G'
            elif obj[42]<=23.51530054644809:
               # {"feature": "C_752400", "instances": 818, "metric_value": 53.5667, "depth": 5}
               if obj[23]>1.0:
                  return 'G'
               elif obj[23]<=1.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '11111':
         # {"feature": "C_502400", "instances": 862, "metric_value": 54.9565, "depth": 3}
         if obj[5] == 'G':
            # {"feature": "C_906370", "instances": 666, "metric_value": 48.9806, "depth": 4}
            if obj[33]<=13.965465465465465:
               # {"feature": "C_114100", "instances": 340, "metric_value": 34.7636, "depth": 5}
               if obj[41]>0.7160782352941175:
                  return 'G'
               elif obj[41]<=0.7160782352941175:
                  return 'G'
               else:
                  return 'G'
            elif obj[33]>13.965465465465465:
               # {"feature": "C_104320", "instances": 326, "metric_value": 34.5703, "depth": 5}
               if obj[17]<=126.66257668711657:
                  return 'G'
               elif obj[17]>126.66257668711657:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[5] == 'B':
            # {"feature": "C_501200", "instances": 104, "metric_value": 15.2221, "depth": 4}
            if obj[4] == 'B':
               # {"feature": "C_750100", "instances": 53, "metric_value": 11.6652, "depth": 5}
               if obj[19]<=2.0:
                  return 'G'
               elif obj[19]>2.0:
                  return 'B'
               else:
                  return 'G'
            elif obj[4] == 'G':
               # {"feature": "C_116000", "instances": 42, "metric_value": 12.357, "depth": 5}
               if obj[45]>3.0:
                  return 'G'
               elif obj[45]<=3.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[4] == 'I':
               # {"feature": "C_100100", "instances": 9, "metric_value": 5.9907, "depth": 5}
               if obj[12]>1.0:
                  return 'B'
               elif obj[12]<=1.0:
                  return 'G'
               else:
                  return 'B'
            else:
               return 'G'
         elif obj[5] == 'I':
            # {"feature": "C_106880", "instances": 92, "metric_value": 15.189, "depth": 4}
            if obj[10]>2.0:
               # {"feature": "C_100110", "instances": 58, "metric_value": 10.8347, "depth": 5}
               if obj[13]<=2.0:
                  return 'G'
               elif obj[13]>2.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[10]<=2.0:
               # {"feature": "C_114100", "instances": 34, "metric_value": 10.9928, "depth": 5}
               if obj[41]>0.6507411764705883:
                  return 'G'
               elif obj[41]<=0.6507411764705883:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '11110':
         # {"feature": "C_502400", "instances": 451, "metric_value": 37.2544, "depth": 3}
         if obj[5] == 'G':
            # {"feature": "C_106880", "instances": 323, "metric_value": 35.0548, "depth": 4}
            if obj[10]>2.0:
               # {"feature": "C_100000", "instances": 162, "metric_value": 24.5257, "depth": 5}
               if obj[18]>9.0:
                  return 'G'
               elif obj[18]<=9.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[10]<=2.0:
               # {"feature": "C_600160", "instances": 161, "metric_value": 25.0625, "depth": 5}
               if obj[42]<=19.77639751552795:
                  return 'G'
               elif obj[42]>19.77639751552795:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[5] == 'B':
            # {"feature": "C_501200", "instances": 85, "metric_value": 15.5622, "depth": 4}
            if obj[4] == 'B':
               # {"feature": "C_500300", "instances": 42, "metric_value": 9.1344, "depth": 5}
               if obj[2] == 'G':
                  return 'G'
               elif obj[2] == 'B':
                  return 'G'
               elif obj[2] == 'I':
                  return 'B'
               else:
                  return 'G'
            elif obj[4] == 'G':
               # {"feature": "C_110720", "instances": 35, "metric_value": 11.1724, "depth": 5}
               if obj[32]>18.0:
                  return 'G'
               elif obj[32]<=18.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[4] == 'I':
               # {"feature": "C_106880", "instances": 8, "metric_value": 5.4641, "depth": 5}
               if obj[10]>2.0:
                  return 'G'
               elif obj[10]<=2.0:
                  return 'B'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[5] == 'I':
            # {"feature": "C_111660", "instances": 43, "metric_value": 7.5419, "depth": 4}
            if obj[8]<=1.0:
               # {"feature": "C_100110", "instances": 35, "metric_value": 7.0161, "depth": 5}
               if obj[13]<=2.0:
                  return 'G'
               elif obj[13]>2.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[8]>1.0:
               # {"feature": "C_750300", "instances": 8, "metric_value": 5.1559, "depth": 5}
               if obj[20]<=4.0:
                  return 'B'
               elif obj[20]>4.0:
                  return 'G'
               else:
                  return 'B'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '11101':
         # {"feature": "C_502400", "instances": 68, "metric_value": 15.1654, "depth": 3}
         if obj[5] == 'G':
            # {"feature": "C_102800", "instances": 58, "metric_value": 14.2104, "depth": 4}
            if obj[28]<=16.67:
               # {"feature": "C_104320", "instances": 33, "metric_value": 10.1587, "depth": 5}
               if obj[17]<=130.8181818181818:
                  return 'G'
               elif obj[17]>130.8181818181818:
                  return 'G'
               else:
                  return 'G'
            elif obj[28]>16.67:
               return 'G'
            else:
               return 'G'
         elif obj[5] == 'I':
            # {"feature": "C_114900", "instances": 6, "metric_value": 4.5765, "depth": 4}
            if obj[49]<=556.0:
               return 'G'
            elif obj[49]>556.0:
               return 'B'
            else:
               return 'G'
         elif obj[5] == 'B':
            return 'G'
         else:
            return 'G'
      else:
         return 'G'
   elif obj[0] == '01110':
      # {"feature": "C_660570", "instances": 4168, "metric_value": 160.179, "depth": 2}
      if obj[1] == '01110':
         # {"feature": "C_906370", "instances": 2060, "metric_value": 87.6025, "depth": 3}
         if obj[33]>9.485922330097088:
            # {"feature": "C_100110", "instances": 1048, "metric_value": 62.1404, "depth": 4}
            if obj[13]>1.0:
               # {"feature": "C_107480", "instances": 548, "metric_value": 44.7324, "depth": 5}
               if obj[31]<=70.32390510948905:
                  return 'G'
               elif obj[31]>70.32390510948905:
                  return 'G'
               else:
                  return 'G'
            elif obj[13]<=1.0:
               # {"feature": "C_104320", "instances": 500, "metric_value": 43.118, "depth": 5}
               if obj[17]>139.982:
                  return 'G'
               elif obj[17]<=139.982:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[33]<=9.485922330097088:
            # {"feature": "C_102800", "instances": 1012, "metric_value": 61.7379, "depth": 4}
            if obj[28]<=28.57:
               # {"feature": "C_752400", "instances": 507, "metric_value": 43.6172, "depth": 5}
               if obj[23]>1.0:
                  return 'G'
               elif obj[23]<=1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[28]>28.57:
               # {"feature": "C_114100", "instances": 505, "metric_value": 43.701, "depth": 5}
               if obj[41]<=0.6257011881188119:
                  return 'G'
               elif obj[41]>0.6257011881188119:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '11110':
         # {"feature": "C_906370", "instances": 1573, "metric_value": 75.9858, "depth": 3}
         if obj[33]>10.131595677050223:
            # {"feature": "C_104320", "instances": 803, "metric_value": 54.5649, "depth": 4}
            if obj[17]>152.25031133250312:
               # {"feature": "C_110720", "instances": 415, "metric_value": 38.583, "depth": 5}
               if obj[32]<=7.563855421686747:
                  return 'G'
               elif obj[32]>7.563855421686747:
                  return 'G'
               else:
                  return 'G'
            elif obj[17]<=152.25031133250312:
               # {"feature": "C_107480", "instances": 388, "metric_value": 38.5868, "depth": 5}
               if obj[31]>43.69948453608248:
                  return 'G'
               elif obj[31]<=43.69948453608248:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[33]<=10.131595677050223:
            # {"feature": "C_107480", "instances": 770, "metric_value": 52.9026, "depth": 4}
            if obj[31]>85.01727272727273:
               # {"feature": "C_600160", "instances": 386, "metric_value": 37.6692, "depth": 5}
               if obj[42]>29.2720207253886:
                  return 'G'
               elif obj[42]<=29.2720207253886:
                  return 'G'
               else:
                  return 'G'
            elif obj[31]<=85.01727272727273:
               # {"feature": "C_100000", "instances": 384, "metric_value": 37.1505, "depth": 5}
               if obj[18]<=5.0:
                  return 'G'
               elif obj[18]>5.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '11111':
         # {"feature": "C_906370", "instances": 317, "metric_value": 34.4884, "depth": 3}
         if obj[33]>9.788643533123029:
            # {"feature": "C_110720", "instances": 160, "metric_value": 24.0521, "depth": 4}
            if obj[32]<=6.7625:
               # {"feature": "C_100110", "instances": 91, "metric_value": 17.4012, "depth": 5}
               if obj[13]>1.0:
                  return 'G'
               elif obj[13]<=1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[32]>6.7625:
               return 'G'
            else:
               return 'G'
         elif obj[33]<=9.788643533123029:
            # {"feature": "C_502400", "instances": 157, "metric_value": 25.8328, "depth": 4}
            if obj[5] == 'G':
               # {"feature": "C_100120", "instances": 132, "metric_value": 22.6318, "depth": 5}
               if obj[14]>1.0:
                  return 'G'
               elif obj[14]<=1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[5] == 'B':
               return 'G'
            elif obj[5] == 'I':
               return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '01111':
         # {"feature": "C_103380", "instances": 218, "metric_value": 28.4239, "depth": 3}
         if obj[36]<=20.0:
            # {"feature": "C_110720", "instances": 117, "metric_value": 20.9012, "depth": 4}
            if obj[32]>6.0:
               # {"feature": "C_107480", "instances": 60, "metric_value": 14.4815, "depth": 5}
               if obj[31]>88.52333333333333:
                  return 'G'
               elif obj[31]<=88.52333333333333:
                  return 'G'
               else:
                  return 'G'
            elif obj[32]<=6.0:
               return 'G'
            else:
               return 'G'
         elif obj[36]>20.0:
            # {"feature": "C_110720", "instances": 101, "metric_value": 19.3131, "depth": 4}
            if obj[32]>5.0:
               # {"feature": "C_106880", "instances": 52, "metric_value": 13.3095, "depth": 5}
               if obj[10]<=1.0:
                  return 'G'
               elif obj[10]>1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[32]<=5.0:
               return 'G'
            else:
               return 'G'
         else:
            return 'G'
      else:
         return 'G'
   elif obj[0] == '00110':
      # {"feature": "C_660570", "instances": 4040, "metric_value": 188.1659, "depth": 2}
      if obj[1] == '00110':
         # {"feature": "C_650640", "instances": 1879, "metric_value": 82.6556, "depth": 3}
         if obj[25]<=2745.306546035125:
            # {"feature": "C_114100", "instances": 965, "metric_value": 57.7446, "depth": 4}
            if obj[41]>0.7095049740932642:
               # {"feature": "C_114900", "instances": 532, "metric_value": 41.9467, "depth": 5}
               if obj[49]>54.505639097744364:
                  return 'G'
               elif obj[49]<=54.505639097744364:
                  return 'G'
               else:
                  return 'G'
            elif obj[41]<=0.7095049740932642:
               # {"feature": "C_114900", "instances": 433, "metric_value": 39.695, "depth": 5}
               if obj[49]>59.54965357967667:
                  return 'G'
               elif obj[49]<=59.54965357967667:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[25]>2745.306546035125:
            # {"feature": "C_110720", "instances": 914, "metric_value": 59.1413, "depth": 4}
            if obj[32]<=6.898249452954048:
               # {"feature": "C_100000", "instances": 466, "metric_value": 42.0623, "depth": 5}
               if obj[18]>2.0:
                  return 'G'
               elif obj[18]<=2.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[32]>6.898249452954048:
               # {"feature": "C_106880", "instances": 448, "metric_value": 41.5761, "depth": 5}
               if obj[10]<=0.0:
                  return 'G'
               elif obj[10]>0.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '10110':
         # {"feature": "C_114100", "instances": 1304, "metric_value": 66.9195, "depth": 3}
         if obj[41]>0.6354894171779142:
            # {"feature": "C_650640", "instances": 667, "metric_value": 46.7552, "depth": 4}
            if obj[25]<=1180.0224887556221:
               # {"feature": "C_107480", "instances": 361, "metric_value": 32.8255, "depth": 5}
               if obj[31]<=46.17922437673129:
                  return 'G'
               elif obj[31]>46.17922437673129:
                  return 'G'
               else:
                  return 'G'
            elif obj[25]>1180.0224887556221:
               # {"feature": "C_100110", "instances": 306, "metric_value": 33.3984, "depth": 5}
               if obj[13]<=1.0:
                  return 'G'
               elif obj[13]>1.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[41]<=0.6354894171779142:
            # {"feature": "C_600160", "instances": 637, "metric_value": 47.9463, "depth": 4}
            if obj[42]>27.747252747252748:
               # {"feature": "C_100120", "instances": 344, "metric_value": 34.5706, "depth": 5}
               if obj[14]>1.0:
                  return 'G'
               elif obj[14]<=1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[42]<=27.747252747252748:
               # {"feature": "C_110720", "instances": 293, "metric_value": 33.2996, "depth": 5}
               if obj[32]<=6.843003412969283:
                  return 'G'
               elif obj[32]>6.843003412969283:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '10111':
         # {"feature": "C_114100", "instances": 302, "metric_value": 29.133, "depth": 3}
         if obj[41]>0.622648013245033:
            # {"feature": "C_500600", "instances": 166, "metric_value": 20.4967, "depth": 4}
            if obj[3] == 'G':
               # {"feature": "C_107480", "instances": 150, "metric_value": 21.9759, "depth": 5}
               if obj[31]<=50.10333333333333:
                  return 'G'
               elif obj[31]>50.10333333333333:
                  return 'G'
               else:
                  return 'G'
            elif obj[3] == 'I':
               # {"feature": "C_106860", "instances": 14, "metric_value": 6.0825, "depth": 5}
               if obj[9]<=4.0:
                  return 'B'
               elif obj[9]>4.0:
                  return 'G'
               else:
                  return 'B'
            elif obj[3] == 'B':
               return 'B'
            else:
               return 'G'
         elif obj[41]<=0.622648013245033:
            # {"feature": "C_103380", "instances": 136, "metric_value": 21.9603, "depth": 4}
            if obj[36]>18.18:
               # {"feature": "C_100140", "instances": 71, "metric_value": 15.4766, "depth": 5}
               if obj[15]<=2.0:
                  return 'G'
               elif obj[15]>2.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[36]<=18.18:
               # {"feature": "C_502400", "instances": 65, "metric_value": 16.552, "depth": 5}
               if obj[5] == 'G':
                  return 'G'
               elif obj[5] == 'B':
                  return 'G'
               elif obj[5] == 'I':
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '00111':
         # {"feature": "C_502400", "instances": 259, "metric_value": 24.9614, "depth": 3}
         if obj[5] == 'G':
            # {"feature": "C_100110", "instances": 224, "metric_value": 26.4195, "depth": 4}
            if obj[13]<=99.0:
               # {"feature": "C_106880", "instances": 199, "metric_value": 27.3685, "depth": 5}
               if obj[10]<=1.0:
                  return 'G'
               elif obj[10]>1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[13]>99.0:
               return 'B'
            else:
               return 'G'
         elif obj[5] == 'I':
            # {"feature": "C_930623", "instances": 28, "metric_value": 8.1017, "depth": 4}
            if obj[27]>-32.64:
               # {"feature": "C_107480", "instances": 26, "metric_value": 8.7148, "depth": 5}
               if obj[31]<=37.2:
                  return 'G'
               elif obj[31]>37.2:
                  return 'G'
               else:
                  return 'G'
            elif obj[27]<=-32.64:
               return 'B'
            else:
               return 'G'
         elif obj[5] == 'B':
            return 'G'
         else:
            return 'G'
      elif obj[1] == '11110':
         # {"feature": "C_100120", "instances": 126, "metric_value": 22.0963, "depth": 3}
         if obj[14]<=1.0:
            # {"feature": "C_600160", "instances": 65, "metric_value": 15.6345, "depth": 4}
            if obj[42]>21.56923076923077:
               # {"feature": "C_502400", "instances": 35, "metric_value": 11.4142, "depth": 5}
               if obj[5] == 'G':
                  return 'G'
               elif obj[5] == 'B':
                  return 'G'
               elif obj[5] == 'I':
                  return 'B'
               else:
                  return 'G'
            elif obj[42]<=21.56923076923077:
               return 'G'
            else:
               return 'G'
         elif obj[14]>1.0:
            return 'G'
         else:
            return 'G'
      elif obj[1] == '01110':
         return 'G'
      elif obj[1] == '11111':
         return 'G'
      elif obj[1] == '01111':
         return 'G'
      else:
         return 'G'
   elif obj[0] == '01100':
      # {"feature": "C_660570", "instances": 4013, "metric_value": 195.8511, "depth": 2}
      if obj[1] == '01100':
         # {"feature": "C_906370", "instances": 1759, "metric_value": 80.5858, "depth": 3}
         if obj[33]<=8.436043206367254:
            # {"feature": "C_107480", "instances": 950, "metric_value": 59.0556, "depth": 4}
            if obj[31]>74.9522105263158:
               # {"feature": "C_114100", "instances": 479, "metric_value": 40.6511, "depth": 5}
               if obj[41]>0.5246200417536535:
                  return 'G'
               elif obj[41]<=0.5246200417536535:
                  return 'G'
               else:
                  return 'G'
            elif obj[31]<=74.9522105263158:
               # {"feature": "C_114900", "instances": 471, "metric_value": 42.8309, "depth": 5}
               if obj[49]>387.5944798301486:
                  return 'G'
               elif obj[49]<=387.5944798301486:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[33]>8.436043206367254:
            # {"feature": "C_100110", "instances": 809, "metric_value": 54.9036, "depth": 4}
            if obj[13]<=1.0:
               # {"feature": "C_114100", "instances": 418, "metric_value": 39.1506, "depth": 5}
               if obj[41]>0.9055052631578948:
                  return 'G'
               elif obj[41]<=0.9055052631578948:
                  return 'G'
               else:
                  return 'G'
            elif obj[13]>1.0:
               # {"feature": "C_100000", "instances": 391, "metric_value": 37.9141, "depth": 5}
               if obj[18]>3.0:
                  return 'G'
               elif obj[18]<=3.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '11100':
         # {"feature": "C_906370", "instances": 1312, "metric_value": 68.7407, "depth": 3}
         if obj[33]<=8.336890243902438:
            # {"feature": "C_106880", "instances": 700, "metric_value": 50.6402, "depth": 4}
            if obj[10]>1.0:
               # {"feature": "C_102800", "instances": 354, "metric_value": 36.7794, "depth": 5}
               if obj[28]>22.22:
                  return 'G'
               elif obj[28]<=22.22:
                  return 'G'
               else:
                  return 'G'
            elif obj[10]<=1.0:
               # {"feature": "C_752400", "instances": 346, "metric_value": 34.8609, "depth": 5}
               if obj[23]>1.0:
                  return 'G'
               elif obj[23]<=1.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[33]>8.336890243902438:
            # {"feature": "C_100110", "instances": 612, "metric_value": 46.5624, "depth": 4}
            if obj[13]<=1.0:
               # {"feature": "C_752400", "instances": 323, "metric_value": 33.4931, "depth": 5}
               if obj[23]>1.0:
                  return 'G'
               elif obj[23]<=1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[13]>1.0:
               # {"feature": "C_114100", "instances": 289, "metric_value": 32.3561, "depth": 5}
               if obj[41]<=0.8888342560553634:
                  return 'G'
               elif obj[41]>0.8888342560553634:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '11111':
         # {"feature": "C_104320", "instances": 304, "metric_value": 31.992, "depth": 3}
         if obj[17]>147.11184210526315:
            # {"feature": "C_502400", "instances": 173, "metric_value": 23.003, "depth": 4}
            if obj[5] == 'G':
               # {"feature": "C_103380", "instances": 121, "metric_value": 21.6372, "depth": 5}
               if obj[36]>16.67:
                  return 'G'
               elif obj[36]<=16.67:
                  return 'G'
               else:
                  return 'G'
            elif obj[5] == 'B':
               # {"feature": "C_111600", "instances": 37, "metric_value": 9.1623, "depth": 5}
               if obj[48]<=0.0:
                  return 'G'
               elif obj[48]>0.0:
                  return 'B'
               else:
                  return 'G'
            elif obj[5] == 'I':
               # {"feature": "C_107480", "instances": 15, "metric_value": 7.3485, "depth": 5}
               if obj[31]>63.4:
                  return 'G'
               elif obj[31]<=63.4:
                  return 'B'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[17]<=147.11184210526315:
            return 'G'
         else:
            return 'G'
      elif obj[1] == '01111':
         # {"feature": "C_502400", "instances": 220, "metric_value": 29.1722, "depth": 3}
         if obj[5] == 'G':
            # {"feature": "C_103380", "instances": 188, "metric_value": 26.2611, "depth": 4}
            if obj[36]<=28.57:
               # {"feature": "C_906370", "instances": 97, "metric_value": 18.4828, "depth": 5}
               if obj[33]>9.0:
                  return 'G'
               elif obj[33]<=9.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[36]>28.57:
               # {"feature": "C_906370", "instances": 91, "metric_value": 18.6633, "depth": 5}
               if obj[33]<=6.0:
                  return 'G'
               elif obj[33]>6.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[5] == 'I':
            # {"feature": "C_501200", "instances": 16, "metric_value": 7.0418, "depth": 4}
            if obj[4] == 'I':
               # {"feature": "C_106860", "instances": 10, "metric_value": 5.6569, "depth": 5}
               if obj[9]<=2.0:
                  return 'G'
               elif obj[9]>2.0:
                  return 'B'
               else:
                  return 'G'
            elif obj[4] == 'G':
               return 'G'
            else:
               return 'G'
         elif obj[5] == 'B':
            return 'G'
         else:
            return 'G'
      elif obj[1] == '01110':
         # {"feature": "C_502400", "instances": 200, "metric_value": 28.783, "depth": 3}
         if obj[5] == 'G':
            return 'G'
         elif obj[5] == 'B':
            # {"feature": "C_500600", "instances": 36, "metric_value": 13.4003, "depth": 4}
            if obj[3] == 'G':
               return 'G'
            elif obj[3] == 'B':
               return 'G'
            elif obj[3] == 'I':
               return 'B'
            else:
               return 'G'
         elif obj[5] == 'I':
            return 'G'
         else:
            return 'G'
      elif obj[1] == '11110':
         # {"feature": "C_502400", "instances": 165, "metric_value": 23.1114, "depth": 3}
         if obj[5] == 'G':
            return 'G'
         elif obj[5] == 'B':
            # {"feature": "C_500600", "instances": 37, "metric_value": 11.7119, "depth": 4}
            if obj[3] == 'G':
               # {"feature": "C_501200", "instances": 23, "metric_value": 10.2211, "depth": 5}
               if obj[4] == 'G':
                  return 'G'
               elif obj[4] == 'B':
                  return 'G'
               elif obj[4] == 'I':
                  return 'G'
               else:
                  return 'G'
            elif obj[3] == 'B':
               # {"feature": "C_111600", "instances": 9, "metric_value": 5.7417, "depth": 5}
               if obj[48]<=0.0:
                  return 'G'
               elif obj[48]>0.0:
                  return 'B'
               else:
                  return 'G'
            elif obj[3] == 'I':
               return 'B'
            else:
               return 'G'
         elif obj[5] == 'I':
            # {"feature": "C_500300", "instances": 7, "metric_value": 4.8783, "depth": 4}
            if obj[2] == 'G':
               return 'G'
            elif obj[2] == 'I':
               return 'B'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '11101':
         # {"feature": "C_502400", "instances": 27, "metric_value": 8.4121, "depth": 3}
         if obj[5] == 'G':
            # {"feature": "C_106880", "instances": 14, "metric_value": 5.7288, "depth": 4}
            if obj[10]<=5.0:
               # {"feature": "C_107480", "instances": 13, "metric_value": 6.3132, "depth": 5}
               if obj[31]<=115.2:
                  return 'G'
               elif obj[31]>115.2:
                  return 'B'
               else:
                  return 'G'
            elif obj[10]>5.0:
               return 'B'
            else:
               return 'G'
         elif obj[5] == 'B':
            return 'G'
         elif obj[5] == 'I':
            # {"feature": "C_106860", "instances": 5, "metric_value": 2.8284, "depth": 4}
            if obj[9]<=3.0:
               # {"feature": "C_106880", "instances": 4, "metric_value": 3.8637, "depth": 5}
               if obj[10]>2.0:
                  return 'G'
               elif obj[10]<=2.0:
                  return 'B'
               else:
                  return 'G'
            elif obj[9]>3.0:
               return 'B'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '01101':
         # {"feature": "C_100000", "instances": 26, "metric_value": 9.4373, "depth": 3}
         if obj[18]<=4.0:
            # {"feature": "C_104320", "instances": 15, "metric_value": 6.7639, "depth": 4}
            if obj[17]<=171.0:
               # {"feature": "C_650640", "instances": 9, "metric_value": 5.4142, "depth": 5}
               if obj[25]>0.0:
                  return 'G'
               elif obj[25]<=0.0:
                  return 'B'
               else:
                  return 'G'
            elif obj[17]>171.0:
               return 'G'
            else:
               return 'G'
         elif obj[18]>4.0:
            return 'G'
         else:
            return 'G'
      else:
         return 'G'
   elif obj[0] == '01111':
      # {"feature": "C_106880", "instances": 3790, "metric_value": 115.2087, "depth": 2}
      if obj[10]<=1.0:
         # {"feature": "C_752400", "instances": 1943, "metric_value": 81.4384, "depth": 3}
         if obj[23]<=0.0:
            # {"feature": "C_100000", "instances": 1003, "metric_value": 58.3466, "depth": 4}
            if obj[18]>4.0:
               # {"feature": "C_116000", "instances": 544, "metric_value": 41.2734, "depth": 5}
               if obj[45]>3.0:
                  return 'G'
               elif obj[45]<=3.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[18]<=4.0:
               # {"feature": "C_650640", "instances": 459, "metric_value": 41.3583, "depth": 5}
               if obj[25]<=1523.2374727668846:
                  return 'G'
               elif obj[25]>1523.2374727668846:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[23]>0.0:
            # {"feature": "C_100000", "instances": 940, "metric_value": 56.8903, "depth": 4}
            if obj[18]>5.0:
               # {"feature": "C_104320", "instances": 482, "metric_value": 40.1193, "depth": 5}
               if obj[17]<=223.64730290456433:
                  return 'G'
               elif obj[17]>223.64730290456433:
                  return 'G'
               else:
                  return 'G'
            elif obj[18]<=5.0:
               # {"feature": "C_906370", "instances": 458, "metric_value": 40.3751, "depth": 5}
               if obj[33]>6.0:
                  return 'G'
               elif obj[33]<=6.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[10]>1.0:
         # {"feature": "C_100100", "instances": 1847, "metric_value": 81.487, "depth": 3}
         if obj[12]>1.0:
            # {"feature": "C_906370", "instances": 928, "metric_value": 57.3948, "depth": 4}
            if obj[33]>11.199353448275861:
               # {"feature": "C_104320", "instances": 487, "metric_value": 40.6998, "depth": 5}
               if obj[17]<=213.48870636550308:
                  return 'G'
               elif obj[17]>213.48870636550308:
                  return 'G'
               else:
                  return 'G'
            elif obj[33]<=11.199353448275861:
               # {"feature": "C_116000", "instances": 441, "metric_value": 40.49, "depth": 5}
               if obj[45]>3.0:
                  return 'G'
               elif obj[45]<=3.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[12]<=1.0:
            # {"feature": "C_107480", "instances": 919, "metric_value": 57.8626, "depth": 4}
            if obj[31]<=81.7746463547334:
               # {"feature": "C_104320", "instances": 480, "metric_value": 41.2649, "depth": 5}
               if obj[17]>143.6875:
                  return 'G'
               elif obj[17]<=143.6875:
                  return 'G'
               else:
                  return 'G'
            elif obj[31]>81.7746463547334:
               # {"feature": "C_502400", "instances": 439, "metric_value": 41.3513, "depth": 5}
               if obj[5] == 'G':
                  return 'G'
               elif obj[5] == 'I':
                  return 'G'
               elif obj[5] == 'B':
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      else:
         return 'G'
   elif obj[0] == '00111':
      # {"feature": "C_660570", "instances": 3347, "metric_value": 132.6733, "depth": 2}
      if obj[1] == '10111':
         # {"feature": "C_104320", "instances": 1651, "metric_value": 70.8835, "depth": 3}
         if obj[17]<=132.91883706844337:
            # {"feature": "C_912070", "instances": 931, "metric_value": 49.2663, "depth": 4}
            if obj[34]>0.0:
               # {"feature": "C_502400", "instances": 507, "metric_value": 32.044, "depth": 5}
               if obj[5] == 'G':
                  return 'G'
               elif obj[5] == 'B':
                  return 'G'
               elif obj[5] == 'I':
                  return 'G'
               else:
                  return 'G'
            elif obj[34]<=0.0:
               # {"feature": "C_106880", "instances": 424, "metric_value": 38.8775, "depth": 5}
               if obj[10]>1.0:
                  return 'G'
               elif obj[10]<=1.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[17]>132.91883706844337:
            # {"feature": "C_502400", "instances": 720, "metric_value": 51.7001, "depth": 4}
            if obj[5] == 'G':
               # {"feature": "C_114100", "instances": 610, "metric_value": 48.2628, "depth": 5}
               if obj[41]<=0.5323427868852459:
                  return 'G'
               elif obj[41]>0.5323427868852459:
                  return 'G'
               else:
                  return 'G'
            elif obj[5] == 'I':
               # {"feature": "C_114100", "instances": 57, "metric_value": 11.6662, "depth": 5}
               if obj[41]<=0.5616280701754387:
                  return 'G'
               elif obj[41]>0.5616280701754387:
                  return 'G'
               else:
                  return 'G'
            elif obj[5] == 'B':
               # {"feature": "C_501200", "instances": 53, "metric_value": 15.9603, "depth": 5}
               if obj[4] == 'B':
                  return 'G'
               elif obj[4] == 'G':
                  return 'G'
               elif obj[4] == 'I':
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '00111':
         # {"feature": "C_100110", "instances": 1364, "metric_value": 67.4188, "depth": 3}
         if obj[13]<=1.0:
            # {"feature": "C_104320", "instances": 743, "metric_value": 47.9588, "depth": 4}
            if obj[17]<=120.83176312247645:
               # {"feature": "C_650640", "instances": 427, "metric_value": 34.8103, "depth": 5}
               if obj[25]<=1192.1007025761123:
                  return 'G'
               elif obj[25]>1192.1007025761123:
                  return 'G'
               else:
                  return 'G'
            elif obj[17]>120.83176312247645:
               # {"feature": "C_906370", "instances": 316, "metric_value": 33.0778, "depth": 5}
               if obj[33]>1.0:
                  return 'G'
               elif obj[33]<=1.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[13]>1.0:
            # {"feature": "C_114100", "instances": 621, "metric_value": 47.4338, "depth": 4}
            if obj[41]>0.6091703703703704:
               # {"feature": "C_100000", "instances": 314, "metric_value": 33.4334, "depth": 5}
               if obj[18]<=4.0:
                  return 'G'
               elif obj[18]>4.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[41]<=0.6091703703703704:
               # {"feature": "C_100140", "instances": 307, "metric_value": 33.6745, "depth": 5}
               if obj[15]>1.0:
                  return 'G'
               elif obj[15]<=1.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '11111':
         # {"feature": "C_502400", "instances": 176, "metric_value": 26.0509, "depth": 3}
         if obj[5] == 'G':
            # {"feature": "C_100120", "instances": 153, "metric_value": 24.4162, "depth": 4}
            if obj[14]>1.0:
               # {"feature": "C_104320", "instances": 77, "metric_value": 17.0994, "depth": 5}
               if obj[17]>234.2987012987013:
                  return 'G'
               elif obj[17]<=234.2987012987013:
                  return 'G'
               else:
                  return 'G'
            elif obj[14]<=1.0:
               return 'G'
            else:
               return 'G'
         elif obj[5] == 'I':
            # {"feature": "C_751200", "instances": 13, "metric_value": 6.3132, "depth": 4}
            if obj[22]<=3.0:
               return 'G'
            elif obj[22]>3.0:
               return 'B'
            else:
               return 'G'
         elif obj[5] == 'B':
            return 'G'
         else:
            return 'G'
      elif obj[1] == '01111':
         # {"feature": "C_100000", "instances": 156, "metric_value": 23.7253, "depth": 3}
         if obj[18]>5.0:
            # {"feature": "C_110720", "instances": 83, "metric_value": 16.5316, "depth": 4}
            if obj[32]>4.0:
               # {"feature": "C_100100", "instances": 48, "metric_value": 11.6793, "depth": 5}
               if obj[12]<=1.0:
                  return 'G'
               elif obj[12]>1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[32]<=4.0:
               return 'G'
            else:
               return 'G'
         elif obj[18]<=5.0:
            return 'G'
         else:
            return 'G'
      else:
         return 'G'
   elif obj[0] == '10001':
      # {"feature": "C_660570", "instances": 1046, "metric_value": 82.1988, "depth": 2}
      if obj[1] == '10001':
         # {"feature": "C_114100", "instances": 729, "metric_value": 50.9152, "depth": 3}
         if obj[41]>0.5604709190672154:
            # {"feature": "C_106860", "instances": 394, "metric_value": 36.3118, "depth": 4}
            if obj[9]>1.0:
               # {"feature": "C_906170", "instances": 204, "metric_value": 24.4428, "depth": 5}
               if obj[26]>0.0:
                  return 'G'
               elif obj[26]<=0.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[9]<=1.0:
               # {"feature": "C_600160", "instances": 190, "metric_value": 26.9841, "depth": 5}
               if obj[42]<=20.378947368421052:
                  return 'G'
               elif obj[42]>20.378947368421052:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[41]<=0.5604709190672154:
            # {"feature": "C_752400", "instances": 335, "metric_value": 35.7343, "depth": 4}
            if obj[23]<=0.0:
               # {"feature": "C_116000", "instances": 171, "metric_value": 25.2329, "depth": 5}
               if obj[45]<=1.0:
                  return 'G'
               elif obj[45]>1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[23]>0.0:
               # {"feature": "C_906370", "instances": 164, "metric_value": 25.2893, "depth": 5}
               if obj[33]<=4.0:
                  return 'G'
               elif obj[33]>4.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '10101':
         # {"feature": "C_912070", "instances": 171, "metric_value": 23.7104, "depth": 3}
         if obj[34]>0.0:
            # {"feature": "C_501200", "instances": 87, "metric_value": 17.2709, "depth": 4}
            if obj[4] == 'G':
               # {"feature": "C_106860", "instances": 78, "metric_value": 16.3411, "depth": 5}
               if obj[9]>1.0:
                  return 'G'
               elif obj[9]<=1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[4] == 'I':
               return 'G'
            elif obj[4] == 'B':
               return 'B'
            else:
               return 'G'
         elif obj[34]<=0.0:
            # {"feature": "C_906370", "instances": 84, "metric_value": 17.0584, "depth": 4}
            if obj[33]>3.0:
               # {"feature": "C_104320", "instances": 46, "metric_value": 11.7954, "depth": 5}
               if obj[17]>154.2391304347826:
                  return 'G'
               elif obj[17]<=154.2391304347826:
                  return 'G'
               else:
                  return 'G'
            elif obj[33]<=3.0:
               return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '10011':
         # {"feature": "C_502400", "instances": 67, "metric_value": 14.3999, "depth": 3}
         if obj[5] == 'G':
            # {"feature": "C_100120", "instances": 54, "metric_value": 13.125, "depth": 4}
            if obj[14]>2.0:
               # {"feature": "C_751200", "instances": 30, "metric_value": 8.9488, "depth": 5}
               if obj[22]>0.0:
                  return 'G'
               elif obj[22]<=0.0:
                  return 'B'
               else:
                  return 'G'
            elif obj[14]<=2.0:
               return 'G'
            else:
               return 'G'
         elif obj[5] == 'I':
            # {"feature": "C_111660", "instances": 8, "metric_value": 5.4641, "depth": 4}
            if obj[8]<=1.0:
               return 'G'
            elif obj[8]>1.0:
               return 'B'
            else:
               return 'G'
         elif obj[5] == 'B':
            return 'G'
         else:
            return 'G'
      elif obj[1] == '11001':
         # {"feature": "C_502400", "instances": 36, "metric_value": 11.318, "depth": 3}
         if obj[5] == 'G':
            # {"feature": "C_906170", "instances": 29, "metric_value": 8.8041, "depth": 4}
            if obj[26]<=4.0:
               # {"feature": "C_104320", "instances": 27, "metric_value": 9.6459, "depth": 5}
               if obj[17]<=219.8148148148148:
                  return 'G'
               elif obj[17]>219.8148148148148:
                  return 'G'
               else:
                  return 'G'
            elif obj[26]>4.0:
               return 'B'
            else:
               return 'G'
         elif obj[5] == 'I':
            return 'G'
         elif obj[5] == 'B':
            return 'G'
         else:
            return 'G'
      elif obj[1] == '10111':
         # {"feature": "C_502400", "instances": 27, "metric_value": 11.7413, "depth": 3}
         if obj[5] == 'G':
            # {"feature": "C_752400", "instances": 14, "metric_value": 6.5132, "depth": 4}
            if obj[23]>1.0:
               return 'G'
            elif obj[23]<=1.0:
               return 'B'
            else:
               return 'G'
         elif obj[5] == 'B':
            return 'G'
         elif obj[5] == 'I':
            return 'G'
         else:
            return 'G'
      elif obj[1] == '11101':
         # {"feature": "C_500600", "instances": 13, "metric_value": 7.3006, "depth": 3}
         if obj[3] == 'G':
            return 'G'
         elif obj[3] == 'B':
            return 'B'
         elif obj[3] == 'I':
            return 'G'
         else:
            return 'G'
      elif obj[1] == '11011':
         # {"feature": "C_500300", "instances": 2, "metric_value": 2.8284, "depth": 3}
         if obj[2] == 'G':
            return 'G'
         elif obj[2] == 'I':
            return 'B'
         else:
            return 'G'
      elif obj[1] == '11111':
         return 'G'
      else:
         return 'G'
   elif obj[0] == '10101':
      # {"feature": "C_660570", "instances": 1033, "metric_value": 60.1192, "depth": 2}
      if obj[1] == '10101':
         # {"feature": "C_114100", "instances": 878, "metric_value": 53.097, "depth": 3}
         if obj[41]>0.6008451025056947:
            # {"feature": "C_107480", "instances": 457, "metric_value": 36.42, "depth": 4}
            if obj[31]<=41.42757111597375:
               # {"feature": "C_752400", "instances": 239, "metric_value": 25.4743, "depth": 5}
               if obj[23]>0.0:
                  return 'G'
               elif obj[23]<=0.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[31]>41.42757111597375:
               # {"feature": "C_100110", "instances": 218, "metric_value": 26.3377, "depth": 5}
               if obj[13]<=3.0:
                  return 'G'
               elif obj[13]>3.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[41]<=0.6008451025056947:
            # {"feature": "C_502400", "instances": 421, "metric_value": 38.9427, "depth": 4}
            if obj[5] == 'G':
               # {"feature": "C_100120", "instances": 354, "metric_value": 36.1408, "depth": 5}
               if obj[14]>3.0:
                  return 'G'
               elif obj[14]<=3.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[5] == 'I':
               # {"feature": "C_100110", "instances": 46, "metric_value": 12.4263, "depth": 5}
               if obj[13]>2.0:
                  return 'G'
               elif obj[13]<=2.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[5] == 'B':
               # {"feature": "C_501200", "instances": 21, "metric_value": 7.4335, "depth": 5}
               if obj[4] == 'G':
                  return 'G'
               elif obj[4] == 'B':
                  return 'G'
               elif obj[4] == 'I':
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '10111':
         # {"feature": "C_502400", "instances": 85, "metric_value": 16.1675, "depth": 3}
         if obj[5] == 'G':
            # {"feature": "C_100000", "instances": 66, "metric_value": 15.2884, "depth": 4}
            if obj[18]>10.0:
               # {"feature": "C_110720", "instances": 36, "metric_value": 10.7235, "depth": 5}
               if obj[32]<=0.0:
                  return 'G'
               elif obj[32]>0.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[18]<=10.0:
               return 'G'
            else:
               return 'G'
         elif obj[5] == 'B':
            # {"feature": "C_111640", "instances": 12, "metric_value": 6.8284, "depth": 4}
            if obj[7]<=0.0:
               return 'G'
            elif obj[7]>0.0:
               return 'B'
            else:
               return 'G'
         elif obj[5] == 'I':
            return 'G'
         else:
            return 'G'
      elif obj[1] == '11101':
         # {"feature": "C_501200", "instances": 64, "metric_value": 15.3123, "depth": 3}
         if obj[4] == 'G':
            return 'G'
         elif obj[4] == 'B':
            return 'B'
         elif obj[4] == 'I':
            return 'G'
         else:
            return 'G'
      elif obj[1] == '11111':
         # {"feature": "C_500600", "instances": 6, "metric_value": 5.8637, "depth": 3}
         if obj[3] == 'G':
            return 'G'
         elif obj[3] == 'B':
            return 'B'
         elif obj[3] == 'I':
            return 'G'
         else:
            return 'G'
      else:
         return 'G'
   elif obj[0] == '00001':
      # {"feature": "C_660570", "instances": 526, "metric_value": 83.9853, "depth": 2}
      if obj[1] == '00001':
         # {"feature": "C_107480", "instances": 217, "metric_value": 27.8451, "depth": 3}
         if obj[31]<=93.89769585253458:
            # {"feature": "C_912070", "instances": 119, "metric_value": 19.9528, "depth": 4}
            if obj[34]<=0.0:
               # {"feature": "C_106820", "instances": 67, "metric_value": 14.9019, "depth": 5}
               if obj[30]>0.0:
                  return 'G'
               elif obj[30]<=0.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[34]>0.0:
               # {"feature": "C_104320", "instances": 52, "metric_value": 13.3246, "depth": 5}
               if obj[17]<=33.03846153846154:
                  return 'G'
               elif obj[17]>33.03846153846154:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[31]>93.89769585253458:
            # {"feature": "C_104320", "instances": 98, "metric_value": 19.3608, "depth": 4}
            if obj[17]<=179.78571428571428:
               return 'G'
            elif obj[17]>179.78571428571428:
               # {"feature": "C_114100", "instances": 45, "metric_value": 12.7474, "depth": 5}
               if obj[41]<=0.0:
                  return 'G'
               elif obj[41]>0.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '10001':
         # {"feature": "C_100120", "instances": 174, "metric_value": 25.7665, "depth": 3}
         if obj[14]>1.0:
            return 'G'
         elif obj[14]<=1.0:
            # {"feature": "C_600160", "instances": 85, "metric_value": 17.5894, "depth": 4}
            if obj[42]>24.341176470588234:
               # {"feature": "C_107480", "instances": 46, "metric_value": 12.4263, "depth": 5}
               if obj[31]<=102.2804347826087:
                  return 'G'
               elif obj[31]>102.2804347826087:
                  return 'G'
               else:
                  return 'G'
            elif obj[42]<=24.341176470588234:
               return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '00101':
         return 'G'
      elif obj[1] == '10101':
         # {"feature": "C_600160", "instances": 25, "metric_value": 8.4888, "depth": 3}
         if obj[42]<=36.0:
            # {"feature": "C_501200", "instances": 15, "metric_value": 6.3585, "depth": 4}
            if obj[4] == 'G':
               # {"feature": "C_502400", "instances": 13, "metric_value": 5.4967, "depth": 5}
               if obj[5] == 'G':
                  return 'G'
               elif obj[5] == 'I':
                  return 'B'
               else:
                  return 'G'
            elif obj[4] == 'B':
               return 'G'
            elif obj[4] == 'I':
               return 'G'
            else:
               return 'G'
         elif obj[42]>36.0:
            return 'G'
         else:
            return 'G'
      elif obj[1] == '11001':
         return 'G'
      elif obj[1] == '00011':
         # {"feature": "C_502400", "instances": 18, "metric_value": 7.9564, "depth": 3}
         if obj[5] == 'G':
            return 'G'
         elif obj[5] == 'B':
            # {"feature": "C_104320", "instances": 3, "metric_value": 3.4142, "depth": 4}
            if obj[17]>50.0:
               return 'G'
            elif obj[17]<=50.0:
               return 'B'
            else:
               return 'G'
         elif obj[5] == 'I':
            return 'G'
         else:
            return 'G'
      elif obj[1] == '10011':
         return 'G'
      elif obj[1] == '01001':
         return 'G'
      elif obj[1] == '10111':
         # {"feature": "C_500600", "instances": 5, "metric_value": 5.2779, "depth": 3}
         if obj[3] == 'G':
            return 'G'
         elif obj[3] == 'I':
            return 'B'
         elif obj[3] == 'B':
            return 'G'
         else:
            return 'G'
      elif obj[1] == '11101':
         return 'G'
      elif obj[1] == '00111':
         return 'G'
      elif obj[1] == '11011':
         return 'G'
      elif obj[1] == '01101':
         return 'G'
      else:
         return 'G'
   elif obj[0] == '11101':
      # {"feature": "C_502400", "instances": 418, "metric_value": 39.0024, "depth": 2}
      if obj[5] == 'G':
         # {"feature": "C_106860", "instances": 326, "metric_value": 33.047, "depth": 3}
         if obj[9]>3.0:
            # {"feature": "C_116000", "instances": 188, "metric_value": 24.0014, "depth": 4}
            if obj[45]>5.0:
               # {"feature": "C_650640", "instances": 117, "metric_value": 17.7102, "depth": 5}
               if obj[25]<=12985.632478632479:
                  return 'G'
               elif obj[25]>12985.632478632479:
                  return 'G'
               else:
                  return 'G'
            elif obj[45]<=5.0:
               # {"feature": "C_100000", "instances": 71, "metric_value": 16.3835, "depth": 5}
               if obj[18]>7.0:
                  return 'G'
               elif obj[18]<=7.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[9]<=3.0:
            # {"feature": "C_100120", "instances": 138, "metric_value": 22.8216, "depth": 4}
            if obj[14]>3.0:
               # {"feature": "C_100110", "instances": 74, "metric_value": 16.2961, "depth": 5}
               if obj[13]<=2.0:
                  return 'G'
               elif obj[13]>2.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[14]<=3.0:
               return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[5] == 'I':
         # {"feature": "C_102800", "instances": 54, "metric_value": 13.1323, "depth": 3}
         if obj[28]<=11.635185185185183:
            # {"feature": "C_912070", "instances": 31, "metric_value": 9.1176, "depth": 4}
            if obj[34]<=5.0:
               # {"feature": "C_100110", "instances": 20, "metric_value": 6.4878, "depth": 5}
               if obj[13]<=5.0:
                  return 'G'
               elif obj[13]>5.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[34]>5.0:
               return 'G'
            else:
               return 'G'
         elif obj[28]>11.635185185185183:
            return 'G'
         else:
            return 'G'
      elif obj[5] == 'B':
         # {"feature": "C_501200", "instances": 38, "metric_value": 10.7445, "depth": 3}
         if obj[4] == 'B':
            # {"feature": "C_114100", "instances": 20, "metric_value": 8.4853, "depth": 4}
            if obj[41]<=0.7094:
               return 'G'
            elif obj[41]>0.7094:
               return 'B'
            else:
               return 'G'
         elif obj[4] == 'G':
            # {"feature": "C_106880", "instances": 16, "metric_value": 7.0418, "depth": 4}
            if obj[10]<=3.0:
               # {"feature": "C_106860", "instances": 10, "metric_value": 5.6569, "depth": 5}
               if obj[9]<=4.0:
                  return 'G'
               elif obj[9]>4.0:
                  return 'B'
               else:
                  return 'G'
            elif obj[10]>3.0:
               return 'G'
            else:
               return 'G'
         elif obj[4] == 'I':
            return 'G'
         else:
            return 'G'
      else:
         return 'G'
   elif obj[0] == '00101':
      # {"feature": "C_660570", "instances": 414, "metric_value": 56.8817, "depth": 2}
      if obj[1] == '00101':
         # {"feature": "C_114100", "instances": 207, "metric_value": 27.111, "depth": 3}
         if obj[41]<=0.4407801932367149:
            # {"feature": "C_116000", "instances": 108, "metric_value": 19.2921, "depth": 4}
            if obj[45]>1.0:
               # {"feature": "C_650640", "instances": 61, "metric_value": 13.6534, "depth": 5}
               if obj[25]<=26095.786885245903:
                  return 'G'
               elif obj[25]>26095.786885245903:
                  return 'G'
               else:
                  return 'G'
            elif obj[45]<=1.0:
               return 'G'
            else:
               return 'G'
         elif obj[41]>0.4407801932367149:
            # {"feature": "C_100110", "instances": 99, "metric_value": 19.1053, "depth": 4}
            if obj[13]>2.0:
               # {"feature": "C_100000", "instances": 51, "metric_value": 13.188, "depth": 5}
               if obj[18]>6.0:
                  return 'G'
               elif obj[18]<=6.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[13]<=2.0:
               return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '10101':
         # {"feature": "C_107480", "instances": 159, "metric_value": 24.5917, "depth": 3}
         if obj[31]<=56.26666666666667:
            # {"feature": "C_100000", "instances": 84, "metric_value": 17.4754, "depth": 4}
            if obj[18]<=7.0:
               # {"feature": "C_650640", "instances": 46, "metric_value": 12.4204, "depth": 5}
               if obj[25]<=6619.217391304348:
                  return 'G'
               elif obj[25]>6619.217391304348:
                  return 'G'
               else:
                  return 'G'
            elif obj[18]>7.0:
               return 'G'
            else:
               return 'G'
         elif obj[31]>56.26666666666667:
            return 'G'
         else:
            return 'G'
      elif obj[1] == '10111':
         return 'G'
      elif obj[1] == '01101':
         return 'G'
      elif obj[1] == '00111':
         return 'G'
      elif obj[1] == '11101':
         return 'G'
      elif obj[1] == '11111':
         return 'G'
      else:
         return 'G'
   elif obj[0] == '11001':
      # {"feature": "C_660570", "instances": 277, "metric_value": 39.4132, "depth": 2}
      if obj[1] == '11001':
         # {"feature": "C_106860", "instances": 186, "metric_value": 25.2244, "depth": 3}
         if obj[9]>2.0:
            # {"feature": "C_502400", "instances": 94, "metric_value": 18.3551, "depth": 4}
            if obj[5] == 'G':
               # {"feature": "C_912070", "instances": 79, "metric_value": 16.4646, "depth": 5}
               if obj[34]>0.0:
                  return 'G'
               elif obj[34]<=0.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[5] == 'I':
               # {"feature": "C_100000", "instances": 10, "metric_value": 5.6569, "depth": 5}
               if obj[18]>4.0:
                  return 'G'
               elif obj[18]<=4.0:
                  return 'B'
               else:
                  return 'G'
            elif obj[5] == 'B':
               return 'G'
            else:
               return 'G'
         elif obj[9]<=2.0:
            # {"feature": "C_104320", "instances": 92, "metric_value": 17.9656, "depth": 4}
            if obj[17]>176.05434782608697:
               # {"feature": "C_906370", "instances": 52, "metric_value": 12.8307, "depth": 5}
               if obj[33]>2.0:
                  return 'G'
               elif obj[33]<=2.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[17]<=176.05434782608697:
               return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[1] == '11101':
         # {"feature": "C_102800", "instances": 48, "metric_value": 12.7388, "depth": 3}
         if obj[28]>14.29:
            # {"feature": "C_650640", "instances": 28, "metric_value": 9.1494, "depth": 4}
            if obj[25]>7000.0:
               # {"feature": "C_100120", "instances": 17, "metric_value": 6.4489, "depth": 5}
               if obj[14]>1.0:
                  return 'G'
               elif obj[14]<=1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[25]<=7000.0:
               return 'G'
            else:
               return 'G'
         elif obj[28]<=14.29:
            return 'G'
         else:
            return 'G'
      elif obj[1] == '11011':
         return 'G'
      elif obj[1] == '11111':
         return 'G'
      else:
         return 'G'
   elif obj[0] == '00000':
      # {"feature": "C_660570", "instances": 174, "metric_value": 49.8854, "depth": 2}
      if obj[1] == '00000':
         # {"feature": "C_107480", "instances": 76, "metric_value": 15.6723, "depth": 3}
         if obj[31]<=10.868421052631579:
            # {"feature": "C_114100", "instances": 43, "metric_value": 10.741, "depth": 4}
            if obj[41]<=0.0:
               # {"feature": "C_104320", "instances": 31, "metric_value": 8.4233, "depth": 5}
               if obj[17]>2.0:
                  return 'G'
               elif obj[17]<=2.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[41]>0.0:
               return 'G'
            else:
               return 'G'
         elif obj[31]>10.868421052631579:
            return 'G'
         else:
            return 'G'
      elif obj[1] == '10000':
         return 'G'
      elif obj[1] == '00011':
         return 'G'
      elif obj[1] == '10011':
         return 'G'
      elif obj[1] == '10111':
         return 'G'
      elif obj[1] == '10010':
         return 'G'
      elif obj[1] == '10100':
         return 'G'
      elif obj[1] == '00111':
         return 'G'
      elif obj[1] == '00100':
         return 'G'
      elif obj[1] == '11011':
         return 'G'
      elif obj[1] == '10101':
         return 'G'
      elif obj[1] == '10110':
         return 'G'
      else:
         return 'G'
   elif obj[0] == '01001':
      # {"feature": "C_660570", "instances": 169, "metric_value": 40.496, "depth": 2}
      if obj[1] == '01001':
         # {"feature": "C_102800", "instances": 51, "metric_value": 11.0638, "depth": 3}
         if obj[28]>33.33:
            # {"feature": "C_106880", "instances": 38, "metric_value": 8.5997, "depth": 4}
            if obj[10]<=0.0:
               # {"feature": "C_912070", "instances": 36, "metric_value": 9.376, "depth": 5}
               if obj[34]<=0.0:
                  return 'G'
               elif obj[34]>0.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[10]>0.0:
               return 'B'
            else:
               return 'G'
         elif obj[28]<=33.33:
            return 'G'
         else:
            return 'G'
      elif obj[1] == '11001':
         # {"feature": "C_906370", "instances": 46, "metric_value": 12.9861, "depth": 3}
         if obj[33]>5.0:
            # {"feature": "C_990370", "instances": 25, "metric_value": 9.226, "depth": 4}
            if obj[40]>-998.0:
               # {"feature": "C_104320", "instances": 14, "metric_value": 6.5132, "depth": 5}
               if obj[17]<=207.0:
                  return 'G'
               elif obj[17]>207.0:
                  return 'B'
               else:
                  return 'G'
            elif obj[40]<=-998.0:
               return 'G'
            else:
               return 'G'
         elif obj[33]<=5.0:
            return 'G'
         else:
            return 'G'
      elif obj[1] == '01011':
         # {"feature": "C_930623", "instances": 18, "metric_value": 7.6569, "depth": 3}
         if obj[27]<=-0.33:
            return 'G'
         elif obj[27]>-0.33:
            return 'B'
         else:
            return 'G'
      elif obj[1] == '11101':
         # {"feature": "C_100120", "instances": 18, "metric_value": 6.7301, "depth": 3}
         if obj[14]<=1.0:
            # {"feature": "C_106860", "instances": 12, "metric_value": 5.2518, "depth": 4}
            if obj[9]<=2.0:
               # {"feature": "C_100160", "instances": 11, "metric_value": 5.501, "depth": 5}
               if obj[16]<=1.0:
                  return 'G'
               elif obj[16]>1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[9]>2.0:
               return 'B'
            else:
               return 'G'
         elif obj[14]>1.0:
            return 'G'
         else:
            return 'G'
      elif obj[1] == '01101':
         return 'G'
      elif obj[1] == '11011':
         # {"feature": "C_106880", "instances": 14, "metric_value": 5.7288, "depth": 3}
         if obj[10]>1.0:
            # {"feature": "C_906170", "instances": 13, "metric_value": 6.3132, "depth": 4}
            if obj[26]<=3.0:
               return 'G'
            elif obj[26]>3.0:
               return 'B'
            else:
               return 'G'
         elif obj[10]<=1.0:
            return 'B'
         else:
            return 'G'
      elif obj[1] == '11111':
         return 'G'
      elif obj[1] == '01111':
         return 'G'
      else:
         return 'G'
   elif obj[0] == '01101':
      # {"feature": "C_660570", "instances": 144, "metric_value": 28.219, "depth": 2}
      if obj[1] == '11101':
         # {"feature": "C_502400", "instances": 67, "metric_value": 14.3937, "depth": 3}
         if obj[5] == 'G':
            # {"feature": "C_650640", "instances": 53, "metric_value": 13.4913, "depth": 4}
            if obj[25]<=8820.981132075472:
               # {"feature": "C_114100", "instances": 31, "metric_value": 9.7505, "depth": 5}
               if obj[41]>0.5289354838709678:
                  return 'G'
               elif obj[41]<=0.5289354838709678:
                  return 'G'
               else:
                  return 'G'
            elif obj[25]>8820.981132075472:
               return 'G'
            else:
               return 'G'
         elif obj[5] == 'I':
            return 'G'
         elif obj[5] == 'B':
            # {"feature": "C_111640", "instances": 5, "metric_value": 4.4495, "depth": 4}
            if obj[7]>0.0:
               return 'B'
            elif obj[7]<=0.0:
               return 'G'
            else:
               return 'B'
         else:
            return 'G'
      elif obj[1] == '01101':
         # {"feature": "C_104320", "instances": 58, "metric_value": 13.7192, "depth": 3}
         if obj[17]>155.75862068965517:
            # {"feature": "C_102800", "instances": 34, "metric_value": 9.7232, "depth": 4}
            if obj[28]>16.67:
               # {"feature": "C_106820", "instances": 22, "metric_value": 7.6921, "depth": 5}
               if obj[30]<=0.0:
                  return 'G'
               elif obj[30]>0.0:
                  return 'B'
               else:
                  return 'G'
            elif obj[28]<=16.67:
               return 'G'
            else:
               return 'G'
         elif obj[17]<=155.75862068965517:
            return 'G'
         else:
            return 'G'
      elif obj[1] == '11111':
         return 'G'
      elif obj[1] == '01111':
         return 'G'
      else:
         return 'G'
   else:
      return 'G'
