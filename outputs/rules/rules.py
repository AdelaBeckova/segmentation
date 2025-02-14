def findDecision(obj): #obj[0]: C_600570, obj[1]: C_660570, obj[2]: C_500300, obj[3]: C_500600, obj[4]: C_501200, obj[5]: C_502400, obj[6]: C_111620, obj[7]: C_111640, obj[8]: C_111660, obj[9]: C_106860, obj[10]: C_106880, obj[11]: C_106920, obj[12]: C_100100, obj[13]: C_100110, obj[14]: C_100120, obj[15]: C_100140, obj[16]: C_100160, obj[17]: C_104320, obj[18]: C_100000, obj[19]: C_750100, obj[20]: C_750300, obj[21]: C_750600, obj[22]: C_751200, obj[23]: C_752400, obj[24]: C_111500, obj[25]: C_650640, obj[26]: C_906170, obj[27]: C_930623, obj[28]: C_102800, obj[29]: C_106800, obj[30]: C_106820, obj[31]: C_107480, obj[32]: C_110720, obj[33]: C_906370, obj[34]: C_912070, obj[35]: C_999032, obj[36]: C_103380, obj[37]: C_106600, obj[38]: C_111300, obj[39]: C_111780, obj[40]: C_990370, obj[41]: C_114100, obj[42]: C_600160, obj[43]: C_961223, obj[44]: C_105740, obj[45]: C_116000, obj[46]: C_990660, obj[47]: C_100900, obj[48]: C_111600, obj[49]: C_114900
   # {"feature": "C_660570", "instances": 60454, "metric_value": 1525.7153, "depth": 1}
   if obj[1] == '10000':
      # {"feature": "C_107480", "instances": 13961, "metric_value": 205.2314, "depth": 2}
      if obj[31]<=25.671384571305783:
         # {"feature": "C_111620", "instances": 7598, "metric_value": 143.5868, "depth": 3}
         if obj[6]>-1.0:
            # {"feature": "C_100000", "instances": 4004, "metric_value": 101.7007, "depth": 4}
            if obj[18]<=2.0:
               # {"feature": "C_751200", "instances": 2066, "metric_value": 73.1057, "depth": 5}
               if obj[22]<=1.0:
                  return 'G'
               elif obj[22]>1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[18]>2.0:
               # {"feature": "C_104320", "instances": 1938, "metric_value": 70.9271, "depth": 5}
               if obj[17]<=33.577399380804955:
                  return 'G'
               elif obj[17]>33.577399380804955:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[6]<=-1.0:
            # {"feature": "C_961223", "instances": 3594, "metric_value": 101.5391, "depth": 4}
            if obj[43]<=-548.7974791318865:
               # {"feature": "C_104320", "instances": 1983, "metric_value": 71.2699, "depth": 5}
               if obj[17]<=12.177508825012607:
                  return 'G'
               elif obj[17]>12.177508825012607:
                  return 'G'
               else:
                  return 'G'
            elif obj[43]>-548.7974791318865:
               # {"feature": "C_100120", "instances": 1611, "metric_value": 72.5236, "depth": 5}
               if obj[14]>1.0:
                  return 'G'
               elif obj[14]<=1.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[31]>25.671384571305783:
         # {"feature": "C_990660", "instances": 6363, "metric_value": 146.6954, "depth": 3}
         if obj[46]<=-443.49775891874907:
            # {"feature": "C_111640", "instances": 3317, "metric_value": 104.9664, "depth": 4}
            if obj[7]>-1.0:
               # {"feature": "C_906370", "instances": 1692, "metric_value": 75.3274, "depth": 5}
               if obj[33]<=3.274822695035461:
                  return 'G'
               elif obj[33]>3.274822695035461:
                  return 'G'
               else:
                  return 'G'
            elif obj[7]<=-1.0:
               # {"feature": "C_600160", "instances": 1625, "metric_value": 73.0773, "depth": 5}
               if obj[42]>31.521846153846155:
                  return 'G'
               elif obj[42]<=31.521846153846155:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[46]>-443.49775891874907:
            # {"feature": "C_906370", "instances": 3046, "metric_value": 102.49, "depth": 4}
            if obj[33]>4.612934996717006:
               # {"feature": "C_106860", "instances": 1538, "metric_value": 71.3842, "depth": 5}
               if obj[9]<=1.0:
                  return 'G'
               elif obj[9]>1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[33]<=4.612934996717006:
               # {"feature": "C_100120", "instances": 1508, "metric_value": 73.5118, "depth": 5}
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
   elif obj[1] == '10011':
      # {"feature": "C_600570", "instances": 7748, "metric_value": 231.0067, "depth": 2}
      if obj[0] == '10011':
         # {"feature": "C_912070", "instances": 4732, "metric_value": 127.0809, "depth": 3}
         if obj[34]>0.0:
            # {"feature": "C_107480", "instances": 2516, "metric_value": 89.5373, "depth": 4}
            if obj[31]<=38.0922893481717:
               # {"feature": "C_100140", "instances": 1471, "metric_value": 64.8211, "depth": 5}
               if obj[15]<=1.0:
                  return 'G'
               elif obj[15]>1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[31]>38.0922893481717:
               # {"feature": "C_110720", "instances": 1045, "metric_value": 61.8343, "depth": 5}
               if obj[32]<=0.0:
                  return 'G'
               elif obj[32]>0.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[34]<=0.0:
            # {"feature": "C_600160", "instances": 2216, "metric_value": 90.307, "depth": 4}
            if obj[42]>28.60965703971119:
               # {"feature": "C_116000", "instances": 1141, "metric_value": 65.1924, "depth": 5}
               if obj[45]<=2.0:
                  return 'G'
               elif obj[45]>2.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[42]<=28.60965703971119:
               # {"feature": "C_100140", "instances": 1075, "metric_value": 62.4925, "depth": 5}
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
      elif obj[0] == '10000':
         # {"feature": "C_107480", "instances": 1247, "metric_value": 62.9593, "depth": 3}
         if obj[31]<=39.525661587810745:
            # {"feature": "C_100120", "instances": 741, "metric_value": 46.4339, "depth": 4}
            if obj[14]<=4.919028340080971:
               # {"feature": "C_906370", "instances": 428, "metric_value": 33.4876, "depth": 5}
               if obj[33]<=4.0:
                  return 'G'
               elif obj[33]>4.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[14]>4.919028340080971:
               # {"feature": "C_104320", "instances": 313, "metric_value": 32.2532, "depth": 5}
               if obj[17]<=66.86900958466454:
                  return 'G'
               elif obj[17]>66.86900958466454:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[31]>39.525661587810745:
            # {"feature": "C_750100", "instances": 506, "metric_value": 42.6688, "depth": 4}
            if obj[19]>1.0:
               # {"feature": "C_906370", "instances": 264, "metric_value": 30.7773, "depth": 5}
               if obj[33]<=4.0:
                  return 'G'
               elif obj[33]>4.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[19]<=1.0:
               # {"feature": "C_751200", "instances": 242, "metric_value": 29.6027, "depth": 5}
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
      elif obj[0] == '00011':
         # {"feature": "C_990660", "instances": 832, "metric_value": 54.6524, "depth": 3}
         if obj[46]<=-1000.0:
            # {"feature": "C_114100", "instances": 433, "metric_value": 38.5497, "depth": 4}
            if obj[41]>0.0:
               # {"feature": "C_100000", "instances": 219, "metric_value": 26.3707, "depth": 5}
               if obj[18]<=3.0:
                  return 'G'
               elif obj[18]>3.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[41]<=0.0:
               # {"feature": "C_100120", "instances": 214, "metric_value": 28.1659, "depth": 5}
               if obj[14]>1.0:
                  return 'G'
               elif obj[14]<=1.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[46]>-1000.0:
            # {"feature": "C_999032", "instances": 399, "metric_value": 38.7388, "depth": 4}
            if obj[35]<=0.0:
               # {"feature": "C_750100", "instances": 218, "metric_value": 28.1607, "depth": 5}
               if obj[19]>1.0:
                  return 'G'
               elif obj[19]<=1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[35]>0.0:
               # {"feature": "C_906370", "instances": 181, "metric_value": 26.6106, "depth": 5}
               if obj[33]>0.0:
                  return 'G'
               elif obj[33]<=0.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[0] == '10010':
         # {"feature": "C_116000", "instances": 559, "metric_value": 45.4249, "depth": 3}
         if obj[45]<=2.0:
            # {"feature": "C_114100", "instances": 280, "metric_value": 32.5121, "depth": 4}
            if obj[41]>0.5976796428571429:
               # {"feature": "C_906370", "instances": 146, "metric_value": 23.175, "depth": 5}
               if obj[33]<=6.0:
                  return 'G'
               elif obj[33]>6.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[41]<=0.5976796428571429:
               # {"feature": "C_100120", "instances": 134, "metric_value": 22.8078, "depth": 5}
               if obj[14]<=2.0:
                  return 'G'
               elif obj[14]>2.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[45]>2.0:
            # {"feature": "C_106880", "instances": 279, "metric_value": 31.7627, "depth": 4}
            if obj[10]<=2.0:
               # {"feature": "C_107480", "instances": 156, "metric_value": 22.7703, "depth": 5}
               if obj[31]<=43.12692307692308:
                  return 'G'
               elif obj[31]>43.12692307692308:
                  return 'G'
               else:
                  return 'G'
            elif obj[10]>2.0:
               return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[0] == '00010':
         return 'G'
      elif obj[0] == '10001':
         # {"feature": "C_100120", "instances": 12, "metric_value": 6.1046, "depth": 3}
         if obj[14]<=5.0:
            return 'G'
         elif obj[14]>5.0:
            return 'B'
         else:
            return 'G'
      elif obj[0] == '00000':
         return 'G'
      elif obj[0] == '00001':
         return 'G'
      else:
         return 'G'
   elif obj[1] == '10010':
      # {"feature": "C_600570", "instances": 4674, "metric_value": 141.9288, "depth": 2}
      if obj[0] == '10010':
         # {"feature": "C_750100", "instances": 3437, "metric_value": 112.4649, "depth": 3}
         if obj[19]<=1.0:
            # {"feature": "C_111660", "instances": 1784, "metric_value": 80.6897, "depth": 4}
            if obj[8]>-1.0:
               # {"feature": "C_600160", "instances": 906, "metric_value": 57.0086, "depth": 5}
               if obj[42]<=23.327814569536425:
                  return 'G'
               elif obj[42]>23.327814569536425:
                  return 'G'
               else:
                  return 'G'
            elif obj[8]<=-1.0:
               # {"feature": "C_600160", "instances": 878, "metric_value": 57.1027, "depth": 5}
               if obj[42]<=0.0:
                  return 'G'
               elif obj[42]>0.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[19]>1.0:
            # {"feature": "C_116000", "instances": 1653, "metric_value": 78.3613, "depth": 4}
            if obj[45]<=2.0:
               # {"feature": "C_600160", "instances": 858, "metric_value": 56.0032, "depth": 5}
               if obj[42]<=25.821678321678323:
                  return 'G'
               elif obj[42]>25.821678321678323:
                  return 'G'
               else:
                  return 'G'
            elif obj[45]>2.0:
               # {"feature": "C_906370", "instances": 795, "metric_value": 54.839, "depth": 5}
               if obj[33]>11.982389937106918:
                  return 'G'
               elif obj[33]<=11.982389937106918:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[0] == '00010':
         # {"feature": "C_100120", "instances": 918, "metric_value": 59.412, "depth": 3}
         if obj[14]<=1.0:
            # {"feature": "C_750100", "instances": 471, "metric_value": 42.1177, "depth": 4}
            if obj[19]>0.0:
               # {"feature": "C_111640", "instances": 239, "metric_value": 29.6264, "depth": 5}
               if obj[7]<=-1.0:
                  return 'G'
               elif obj[7]>-1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[19]<=0.0:
               # {"feature": "C_111500", "instances": 232, "metric_value": 29.9352, "depth": 5}
               if obj[24]<=-1.0:
                  return 'G'
               elif obj[24]>-1.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[14]>1.0:
            # {"feature": "C_751200", "instances": 447, "metric_value": 41.9063, "depth": 4}
            if obj[22]>1.0:
               # {"feature": "C_106880", "instances": 224, "metric_value": 29.6659, "depth": 5}
               if obj[10]>1.0:
                  return 'G'
               elif obj[10]<=1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[22]<=1.0:
               # {"feature": "C_100000", "instances": 223, "metric_value": 29.5996, "depth": 5}
               if obj[18]<=3.0:
                  return 'G'
               elif obj[18]>3.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[0] == '10000':
         # {"feature": "C_104320", "instances": 235, "metric_value": 28.8485, "depth": 3}
         if obj[17]<=134.46382978723403:
            # {"feature": "C_600160", "instances": 131, "metric_value": 20.8279, "depth": 4}
            if obj[42]>34.274809160305345:
               # {"feature": "C_110720", "instances": 72, "metric_value": 14.6554, "depth": 5}
               if obj[32]<=0.0:
                  return 'G'
               elif obj[32]>0.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[42]<=34.274809160305345:
               # {"feature": "C_752400", "instances": 59, "metric_value": 14.8485, "depth": 5}
               if obj[23]<=1.0:
                  return 'G'
               elif obj[23]>1.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[17]>134.46382978723403:
            # {"feature": "C_100120", "instances": 104, "metric_value": 20.0074, "depth": 4}
            if obj[14]>4.0:
               # {"feature": "C_107480", "instances": 54, "metric_value": 14.1616, "depth": 5}
               if obj[31]<=58.411111111111104:
                  return 'G'
               elif obj[31]>58.411111111111104:
                  return 'G'
               else:
                  return 'G'
            elif obj[14]<=4.0:
               return 'G'
            else:
               return 'G'
         else:
            return 'G'
      else:
         return 'G'
   elif obj[1] == '11011':
      # {"feature": "C_600570", "instances": 4522, "metric_value": 253.1658, "depth": 2}
      if obj[0] == '11011':
         # {"feature": "C_906370", "instances": 2404, "metric_value": 97.4756, "depth": 3}
         if obj[33]<=11.262895174708818:
            # {"feature": "C_114100", "instances": 1320, "metric_value": 72.0053, "depth": 4}
            if obj[41]>0.6785632575757576:
               # {"feature": "C_110720", "instances": 677, "metric_value": 51.1236, "depth": 5}
               if obj[32]<=0.0:
                  return 'G'
               elif obj[32]>0.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[41]<=0.6785632575757576:
               return 'G'
            else:
               return 'G'
         elif obj[33]>11.262895174708818:
            return 'G'
         else:
            return 'G'
      elif obj[0] == '01011':
         # {"feature": "C_100000", "instances": 689, "metric_value": 51.8847, "depth": 3}
         if obj[18]<=5.0:
            # {"feature": "C_107480", "instances": 357, "metric_value": 37.1525, "depth": 4}
            if obj[31]>112.13333333333331:
               # {"feature": "C_906370", "instances": 180, "metric_value": 26.5212, "depth": 5}
               if obj[33]<=0.0:
                  return 'G'
               elif obj[33]>0.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[31]<=112.13333333333331:
               # {"feature": "C_110720", "instances": 177, "metric_value": 26.0099, "depth": 5}
               if obj[32]<=0.0:
                  return 'G'
               elif obj[32]>0.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[18]>5.0:
            # {"feature": "C_100100", "instances": 332, "metric_value": 36.2186, "depth": 4}
            if obj[12]<=1.0:
               # {"feature": "C_103380", "instances": 173, "metric_value": 26.0033, "depth": 5}
               if obj[36]<=0.0:
                  return 'G'
               elif obj[36]>0.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[12]>1.0:
               return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[0] == '11000':
         # {"feature": "C_100000", "instances": 453, "metric_value": 41.8125, "depth": 3}
         if obj[18]<=6.0:
            # {"feature": "C_750100", "instances": 232, "metric_value": 29.9422, "depth": 4}
            if obj[19]>1.0:
               # {"feature": "C_100120", "instances": 120, "metric_value": 21.1753, "depth": 5}
               if obj[14]>2.0:
                  return 'G'
               elif obj[14]<=2.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[19]<=1.0:
               return 'G'
            else:
               return 'G'
         elif obj[18]>6.0:
            # {"feature": "C_106860", "instances": 221, "metric_value": 29.1963, "depth": 4}
            if obj[9]<=2.0:
               # {"feature": "C_100140", "instances": 117, "metric_value": 20.8981, "depth": 5}
               if obj[15]<=1.0:
                  return 'G'
               elif obj[15]>1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[9]>2.0:
               return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[0] == '11010':
         # {"feature": "C_116000", "instances": 351, "metric_value": 37.2567, "depth": 3}
         if obj[45]<=3.0:
            # {"feature": "C_104320", "instances": 179, "metric_value": 26.4607, "depth": 4}
            if obj[17]>157.08379888268158:
               # {"feature": "C_107480", "instances": 91, "metric_value": 18.6633, "depth": 5}
               if obj[31]<=91.47362637362636:
                  return 'G'
               elif obj[31]>91.47362637362636:
                  return 'G'
               else:
                  return 'G'
            elif obj[17]<=157.08379888268158:
               return 'G'
            else:
               return 'G'
         elif obj[45]>3.0:
            return 'G'
         else:
            return 'G'
      elif obj[0] == '10011':
         # {"feature": "C_100000", "instances": 185, "metric_value": 26.9094, "depth": 3}
         if obj[18]<=7.0:
            # {"feature": "C_906370", "instances": 96, "metric_value": 19.1917, "depth": 4}
            if obj[33]>4.0:
               # {"feature": "C_100120", "instances": 50, "metric_value": 13.5865, "depth": 5}
               if obj[14]>2.0:
                  return 'G'
               elif obj[14]<=2.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[33]<=4.0:
               return 'G'
            else:
               return 'G'
         elif obj[18]>7.0:
            return 'G'
         else:
            return 'G'
      elif obj[0] == '01000':
         # {"feature": "C_100120", "instances": 146, "metric_value": 23.8282, "depth": 3}
         if obj[14]>1.0:
            return 'G'
         elif obj[14]<=1.0:
            # {"feature": "C_990660", "instances": 71, "metric_value": 16.3835, "depth": 4}
            if obj[46]>-363.6350704225352:
               # {"feature": "C_104320", "instances": 37, "metric_value": 11.5231, "depth": 5}
               if obj[17]<=138.7027027027027:
                  return 'G'
               elif obj[17]>138.7027027027027:
                  return 'G'
               else:
                  return 'G'
            elif obj[46]<=-363.6350704225352:
               return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[0] == '01010':
         # {"feature": "C_106880", "instances": 119, "metric_value": 21.4516, "depth": 3}
         if obj[10]<=2.0:
            # {"feature": "C_906370", "instances": 63, "metric_value": 15.3776, "depth": 4}
            if obj[33]<=5.0:
               # {"feature": "C_100000", "instances": 33, "metric_value": 10.8106, "depth": 5}
               if obj[18]<=5.0:
                  return 'G'
               elif obj[18]>5.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[33]>5.0:
               return 'G'
            else:
               return 'G'
         elif obj[10]>2.0:
            return 'G'
         else:
            return 'G'
      elif obj[0] == '00011':
         return 'G'
      elif obj[0] == '10010':
         return 'G'
      elif obj[0] == '10000':
         return 'G'
      elif obj[0] == '00010':
         return 'G'
      elif obj[0] == '11001':
         return 'G'
      elif obj[0] == '01001':
         return 'G'
      elif obj[0] == '10001':
         return 'G'
      else:
         return 'G'
   elif obj[1] == '11111':
      # {"feature": "C_600570", "instances": 3641, "metric_value": 328.0745, "depth": 2}
      if obj[0] == '11111':
         # {"feature": "C_114100", "instances": 1225, "metric_value": 69.3082, "depth": 3}
         if obj[41]>0.6704810612244899:
            # {"feature": "C_106880", "instances": 638, "metric_value": 49.7276, "depth": 4}
            if obj[10]<=2.0:
               # {"feature": "C_107480", "instances": 325, "metric_value": 35.1774, "depth": 5}
               if obj[31]<=63.835692307692305:
                  return 'G'
               elif obj[31]>63.835692307692305:
                  return 'G'
               else:
                  return 'G'
            elif obj[10]>2.0:
               # {"feature": "C_100140", "instances": 313, "metric_value": 35.157, "depth": 5}
               if obj[15]<=2.0:
                  return 'G'
               elif obj[15]>2.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[41]<=0.6704810612244899:
            # {"feature": "C_106880", "instances": 587, "metric_value": 48.2614, "depth": 4}
            if obj[10]<=2.0:
               # {"feature": "C_107480", "instances": 316, "metric_value": 35.3139, "depth": 5}
               if obj[31]<=97.02753164556961:
                  return 'G'
               elif obj[31]>97.02753164556961:
                  return 'G'
               else:
                  return 'G'
            elif obj[10]>2.0:
               return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[0] == '11011':
         # {"feature": "C_906370", "instances": 659, "metric_value": 51.1379, "depth": 3}
         if obj[33]<=11.802731411229136:
            return 'G'
         elif obj[33]>11.802731411229136:
            # {"feature": "C_106860", "instances": 303, "metric_value": 34.5788, "depth": 4}
            if obj[9]<=3.0:
               # {"feature": "C_100120", "instances": 159, "metric_value": 24.9027, "depth": 5}
               if obj[14]>4.0:
                  return 'G'
               elif obj[14]<=4.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[9]>3.0:
               return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[0] == '01111':
         # {"feature": "C_100120", "instances": 398, "metric_value": 39.4996, "depth": 3}
         if obj[14]>1.0:
            # {"feature": "C_116000", "instances": 206, "metric_value": 28.1529, "depth": 4}
            if obj[45]<=3.0:
               # {"feature": "C_100110", "instances": 106, "metric_value": 19.8273, "depth": 5}
               if obj[13]<=1.0:
                  return 'G'
               elif obj[13]>1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[45]>3.0:
               return 'G'
            else:
               return 'G'
         elif obj[14]<=1.0:
            return 'G'
         else:
            return 'G'
      elif obj[0] == '01011':
         return 'G'
      elif obj[0] == '11110':
         # {"feature": "C_906370", "instances": 181, "metric_value": 26.6114, "depth": 3}
         if obj[33]<=15.07182320441989:
            # {"feature": "C_104320", "instances": 93, "metric_value": 18.8745, "depth": 4}
            if obj[17]>197.44086021505376:
               # {"feature": "C_502400", "instances": 47, "metric_value": 13.5126, "depth": 5}
               if obj[5] == 'G':
                  return 'G'
               elif obj[5] == 'I':
                  return 'G'
               elif obj[5] == 'B':
                  return 'G'
               else:
                  return 'G'
            elif obj[17]<=197.44086021505376:
               return 'G'
            else:
               return 'G'
         elif obj[33]>15.07182320441989:
            return 'G'
         else:
            return 'G'
      elif obj[0] == '11100':
         # {"feature": "C_106860", "instances": 156, "metric_value": 24.6597, "depth": 3}
         if obj[9]>3.0:
            # {"feature": "C_100120", "instances": 78, "metric_value": 17.216, "depth": 4}
            if obj[14]>5.0:
               # {"feature": "C_906370", "instances": 41, "metric_value": 12.1946, "depth": 5}
               if obj[33]<=16.0:
                  return 'G'
               elif obj[33]>16.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[14]<=5.0:
               return 'G'
            else:
               return 'G'
         elif obj[9]<=3.0:
            return 'G'
         else:
            return 'G'
      elif obj[0] == '10111':
         return 'G'
      elif obj[0] == '11010':
         return 'G'
      elif obj[0] == '11000':
         # {"feature": "C_106880", "instances": 103, "metric_value": 19.9069, "depth": 3}
         if obj[10]<=3.0:
            # {"feature": "C_750100", "instances": 54, "metric_value": 14.1616, "depth": 4}
            if obj[19]<=1.0:
               # {"feature": "C_104320", "instances": 29, "metric_value": 10.0488, "depth": 5}
               if obj[17]<=144.68965517241378:
                  return 'G'
               elif obj[17]>144.68965517241378:
                  return 'G'
               else:
                  return 'G'
            elif obj[19]>1.0:
               return 'G'
            else:
               return 'G'
         elif obj[10]>3.0:
            return 'G'
         else:
            return 'G'
      elif obj[0] == '01110':
         return 'G'
      elif obj[0] == '01100':
         # {"feature": "C_100000", "instances": 70, "metric_value": 16.2614, "depth": 3}
         if obj[18]<=6.0:
            # {"feature": "C_906370", "instances": 37, "metric_value": 11.5155, "depth": 4}
            if obj[33]>6.0:
               # {"feature": "C_100100", "instances": 19, "metric_value": 7.8376, "depth": 5}
               if obj[12]<=1.0:
                  return 'G'
               elif obj[12]>1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[33]<=6.0:
               return 'G'
            else:
               return 'G'
         elif obj[18]>6.0:
            return 'G'
         else:
            return 'G'
      elif obj[0] == '10011':
         # {"feature": "C_502400", "instances": 50, "metric_value": 13.7829, "depth": 3}
         if obj[5] == 'G':
            # {"feature": "C_100120", "instances": 44, "metric_value": 12.6754, "depth": 4}
            if obj[14]<=4.0:
               # {"feature": "C_750100", "instances": 24, "metric_value": 9.0077, "depth": 5}
               if obj[19]>0.0:
                  return 'G'
               elif obj[19]<=0.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[14]>4.0:
               return 'G'
            else:
               return 'G'
         elif obj[5] == 'I':
            return 'G'
         elif obj[5] == 'B':
            return 'G'
         else:
            return 'G'
      elif obj[0] == '00111':
         return 'G'
      elif obj[0] == '01010':
         return 'G'
      elif obj[0] == '01000':
         # {"feature": "C_100120", "instances": 29, "metric_value": 10.0488, "depth": 3}
         if obj[14]<=1.0:
            # {"feature": "C_111640", "instances": 16, "metric_value": 7.0418, "depth": 4}
            if obj[7]>-1.0:
               # {"feature": "C_100110", "instances": 10, "metric_value": 5.6569, "depth": 5}
               if obj[13]<=2.0:
                  return 'G'
               elif obj[13]>2.0:
                  return 'B'
               else:
                  return 'G'
            elif obj[7]<=-1.0:
               return 'G'
            else:
               return 'G'
         elif obj[14]>1.0:
            return 'G'
         else:
            return 'G'
      elif obj[0] == '11101':
         return 'G'
      elif obj[0] == '00011':
         return 'G'
      elif obj[0] == '10110':
         return 'G'
      elif obj[0] == '00110':
         return 'G'
      elif obj[0] == '10100':
         return 'G'
      elif obj[0] == '00100':
         return 'G'
      elif obj[0] == '00010':
         return 'G'
      elif obj[0] == '10010':
         return 'G'
      elif obj[0] == '10000':
         return 'G'
      elif obj[0] == '11001':
         return 'G'
      elif obj[0] == '10101':
         return 'G'
      elif obj[0] == '01101':
         return 'G'
      elif obj[0] == '01001':
         return 'G'
      else:
         return 'G'
   elif obj[1] == '10111':
      # {"feature": "C_600570", "instances": 2993, "metric_value": 226.6231, "depth": 2}
      if obj[0] == '10111':
         # {"feature": "C_912070", "instances": 1185, "metric_value": 66.0639, "depth": 3}
         if obj[34]>0.0:
            # {"feature": "C_502400", "instances": 622, "metric_value": 48.5883, "depth": 4}
            if obj[5] == 'G':
               # {"feature": "C_114100", "instances": 540, "metric_value": 43.5617, "depth": 5}
               if obj[41]>0.6932185185185185:
                  return 'G'
               elif obj[41]<=0.6932185185185185:
                  return 'G'
               else:
                  return 'G'
            elif obj[5] == 'I':
               return 'G'
            elif obj[5] == 'B':
               return 'G'
            else:
               return 'G'
         elif obj[34]<=0.0:
            # {"feature": "C_116000", "instances": 563, "metric_value": 46.2724, "depth": 4}
            if obj[45]<=3.0:
               # {"feature": "C_114100", "instances": 284, "metric_value": 33.2248, "depth": 5}
               if obj[41]>0.6335038732394366:
                  return 'G'
               elif obj[41]<=0.6335038732394366:
                  return 'G'
               else:
                  return 'G'
            elif obj[45]>3.0:
               # {"feature": "C_114100", "instances": 279, "metric_value": 32.2067, "depth": 5}
               if obj[41]>0.6781555555555555:
                  return 'G'
               elif obj[41]<=0.6781555555555555:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[0] == '10011':
         # {"feature": "C_912070", "instances": 558, "metric_value": 45.5486, "depth": 3}
         if obj[34]>0.0:
            # {"feature": "C_116000", "instances": 295, "metric_value": 32.7035, "depth": 4}
            if obj[45]<=3.0:
               # {"feature": "C_110720", "instances": 163, "metric_value": 23.9889, "depth": 5}
               if obj[32]<=0.0:
                  return 'G'
               elif obj[32]>0.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[45]>3.0:
               # {"feature": "C_100120", "instances": 132, "metric_value": 22.2896, "depth": 5}
               if obj[14]<=6.0:
                  return 'G'
               elif obj[14]>6.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[34]<=0.0:
            # {"feature": "C_116000", "instances": 263, "metric_value": 31.7014, "depth": 4}
            if obj[45]>2.0:
               # {"feature": "C_110720", "instances": 135, "metric_value": 22.2245, "depth": 5}
               if obj[32]<=7.985185185185185:
                  return 'G'
               elif obj[32]>7.985185185185185:
                  return 'G'
               else:
                  return 'G'
            elif obj[45]<=2.0:
               return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[0] == '10100':
         # {"feature": "C_114100", "instances": 306, "metric_value": 32.0682, "depth": 3}
         if obj[41]>0.6971156862745098:
            # {"feature": "C_100000", "instances": 162, "metric_value": 21.7716, "depth": 4}
            if obj[18]<=9.0:
               # {"feature": "C_906370", "instances": 93, "metric_value": 15.4174, "depth": 5}
               if obj[33]>8.0:
                  return 'G'
               elif obj[33]<=8.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[18]>9.0:
               # {"feature": "C_116000", "instances": 69, "metric_value": 15.6741, "depth": 5}
               if obj[45]<=3.0:
                  return 'G'
               elif obj[45]>3.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[41]<=0.6971156862745098:
            # {"feature": "C_100120", "instances": 144, "metric_value": 23.6689, "depth": 4}
            if obj[14]<=4.0:
               # {"feature": "C_906370", "instances": 74, "metric_value": 16.7433, "depth": 5}
               if obj[33]>3.0:
                  return 'G'
               elif obj[33]<=3.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[14]>4.0:
               return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[0] == '00111':
         # {"feature": "C_104320", "instances": 236, "metric_value": 29.9465, "depth": 3}
         if obj[17]<=151.52966101694915:
            # {"feature": "C_114100", "instances": 119, "metric_value": 20.72, "depth": 4}
            if obj[41]>0.6056655462184873:
               # {"feature": "C_100110", "instances": 61, "metric_value": 14.6245, "depth": 5}
               if obj[13]<=1.0:
                  return 'G'
               elif obj[13]>1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[41]<=0.6056655462184873:
               # {"feature": "C_114900", "instances": 58, "metric_value": 14.7027, "depth": 5}
               if obj[49]>50.0:
                  return 'G'
               elif obj[49]<=50.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[17]>151.52966101694915:
            return 'G'
         else:
            return 'G'
      elif obj[0] == '10000':
         # {"feature": "C_116000", "instances": 160, "metric_value": 24.0401, "depth": 3}
         if obj[45]>1.0:
            # {"feature": "C_114100", "instances": 83, "metric_value": 16.9429, "depth": 4}
            if obj[41]>0.7480301204819279:
               # {"feature": "C_100000", "instances": 47, "metric_value": 12.0442, "depth": 5}
               if obj[18]<=10.0:
                  return 'G'
               elif obj[18]>10.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[41]<=0.7480301204819279:
               return 'G'
            else:
               return 'G'
         elif obj[45]<=1.0:
            # {"feature": "C_100120", "instances": 77, "metric_value": 17.0966, "depth": 4}
            if obj[14]<=3.0:
               # {"feature": "C_906370", "instances": 39, "metric_value": 11.8635, "depth": 5}
               if obj[33]<=3.0:
                  return 'G'
               elif obj[33]>3.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[14]>3.0:
               return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[0] == '10110':
         # {"feature": "C_100000", "instances": 156, "metric_value": 24.6613, "depth": 3}
         if obj[18]<=8.0:
            # {"feature": "C_100120", "instances": 79, "metric_value": 17.331, "depth": 4}
            if obj[14]>2.0:
               # {"feature": "C_110720", "instances": 42, "metric_value": 12.3548, "depth": 5}
               if obj[32]<=10.071428571428571:
                  return 'G'
               elif obj[32]>10.071428571428571:
                  return 'G'
               else:
                  return 'G'
            elif obj[14]<=2.0:
               return 'G'
            else:
               return 'G'
         elif obj[18]>8.0:
            return 'G'
         else:
            return 'G'
      elif obj[0] == '00011':
         # {"feature": "C_104320", "instances": 91, "metric_value": 18.2565, "depth": 3}
         if obj[17]<=163.24175824175825:
            # {"feature": "C_114100", "instances": 49, "metric_value": 12.895, "depth": 4}
            if obj[41]<=0.3054734693877551:
               # {"feature": "C_930623", "instances": 28, "metric_value": 9.1494, "depth": 5}
               if obj[27]<=-74.78:
                  return 'G'
               elif obj[27]>-74.78:
                  return 'G'
               else:
                  return 'G'
            elif obj[41]>0.3054734693877551:
               return 'G'
            else:
               return 'G'
         elif obj[17]>163.24175824175825:
            return 'G'
         else:
            return 'G'
      elif obj[0] == '10010':
         # {"feature": "C_116000", "instances": 90, "metric_value": 18.5564, "depth": 3}
         if obj[45]>2.0:
            # {"feature": "C_100120", "instances": 47, "metric_value": 13.1386, "depth": 4}
            if obj[14]<=6.0:
               # {"feature": "C_906370", "instances": 25, "metric_value": 9.226, "depth": 5}
               if obj[33]>9.0:
                  return 'G'
               elif obj[33]<=9.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[14]>6.0:
               return 'G'
            else:
               return 'G'
         elif obj[45]<=2.0:
            return 'G'
         else:
            return 'G'
      elif obj[0] == '00100':
         # {"feature": "C_906370", "instances": 82, "metric_value": 17.2459, "depth": 3}
         if obj[33]>2.0:
            # {"feature": "C_100110", "instances": 45, "metric_value": 12.2643, "depth": 4}
            if obj[13]<=1.0:
               # {"feature": "C_990660", "instances": 25, "metric_value": 8.4888, "depth": 5}
               if obj[46]<=-14.57:
                  return 'G'
               elif obj[46]>-14.57:
                  return 'G'
               else:
                  return 'G'
            elif obj[13]>1.0:
               return 'G'
            else:
               return 'G'
         elif obj[33]<=2.0:
            return 'G'
         else:
            return 'G'
      elif obj[0] == '00110':
         return 'G'
      elif obj[0] == '00010':
         return 'G'
      elif obj[0] == '10101':
         return 'G'
      elif obj[0] == '10001':
         return 'G'
      elif obj[0] == '00101':
         return 'G'
      elif obj[0] == '00001':
         return 'G'
      else:
         return 'G'
   elif obj[1] == '11010':
      # {"feature": "C_600570", "instances": 2840, "metric_value": 160.2956, "depth": 2}
      if obj[0] == '11010':
         # {"feature": "C_104320", "instances": 1693, "metric_value": 82.0925, "depth": 3}
         if obj[17]>151.6420555227407:
            return 'G'
         elif obj[17]<=151.6420555227407:
            # {"feature": "C_102800", "instances": 831, "metric_value": 57.3766, "depth": 4}
            if obj[28]<=19.1308182912154:
               # {"feature": "C_906370", "instances": 416, "metric_value": 40.582, "depth": 5}
               if obj[33]<=14.733173076923077:
                  return 'G'
               elif obj[33]>14.733173076923077:
                  return 'G'
               else:
                  return 'G'
            elif obj[28]>19.1308182912154:
               # {"feature": "C_750100", "instances": 415, "metric_value": 40.5472, "depth": 5}
               if obj[19]<=1.0:
                  return 'G'
               elif obj[19]>1.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[0] == '01010':
         # {"feature": "C_111620", "instances": 631, "metric_value": 50.0792, "depth": 3}
         if obj[6]<=-1.0:
            return 'G'
         elif obj[6]>-1.0:
            # {"feature": "C_106880", "instances": 313, "metric_value": 35.1582, "depth": 4}
            if obj[10]>1.0:
               # {"feature": "C_104320", "instances": 159, "metric_value": 24.9036, "depth": 5}
               if obj[17]<=157.73584905660377:
                  return 'G'
               elif obj[17]>157.73584905660377:
                  return 'G'
               else:
                  return 'G'
            elif obj[10]<=1.0:
               return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[0] == '11000':
         return 'G'
      elif obj[0] == '10010':
         return 'G'
      elif obj[0] == '01000':
         return 'G'
      elif obj[0] == '00010':
         return 'G'
      elif obj[0] == '10000':
         return 'G'
      else:
         return 'G'
   elif obj[1] == '11000':
      # {"feature": "C_600570", "instances": 2609, "metric_value": 108.3067, "depth": 2}
      if obj[0] == '11000':
         # {"feature": "C_906370", "instances": 1806, "metric_value": 83.5587, "depth": 3}
         if obj[33]<=9.189922480620154:
            # {"feature": "C_100120", "instances": 936, "metric_value": 60.5122, "depth": 4}
            if obj[14]>2.0:
               # {"feature": "C_100000", "instances": 491, "metric_value": 43.9536, "depth": 5}
               if obj[18]<=5.0:
                  return 'G'
               elif obj[18]>5.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[14]<=2.0:
               # {"feature": "C_102800", "instances": 445, "metric_value": 41.6237, "depth": 5}
               if obj[28]>33.33:
                  return 'G'
               elif obj[28]<=33.33:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[33]>9.189922480620154:
            # {"feature": "C_102800", "instances": 870, "metric_value": 57.6219, "depth": 4}
            if obj[28]<=24.327770114942528:
               # {"feature": "C_106600", "instances": 462, "metric_value": 41.6769, "depth": 5}
               if obj[37]>1.0:
                  return 'G'
               elif obj[37]<=1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[28]>24.327770114942528:
               # {"feature": "C_100000", "instances": 408, "metric_value": 39.7965, "depth": 5}
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
      elif obj[0] == '01000':
         # {"feature": "C_111660", "instances": 651, "metric_value": 50.0897, "depth": 3}
         if obj[8]>-1.0:
            # {"feature": "C_102800", "instances": 330, "metric_value": 35.4329, "depth": 4}
            if obj[28]<=33.33:
               # {"feature": "C_100120", "instances": 172, "metric_value": 25.9248, "depth": 5}
               if obj[14]<=2.0:
                  return 'G'
               elif obj[14]>2.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[28]>33.33:
               # {"feature": "C_107480", "instances": 158, "metric_value": 24.2002, "depth": 5}
               if obj[31]<=87.47911392405064:
                  return 'G'
               elif obj[31]>87.47911392405064:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[8]<=-1.0:
            # {"feature": "C_750100", "instances": 321, "metric_value": 35.3886, "depth": 4}
            if obj[19]>0.0:
               # {"feature": "C_100000", "instances": 166, "metric_value": 25.1528, "depth": 5}
               if obj[18]>2.0:
                  return 'G'
               elif obj[18]<=2.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[19]<=0.0:
               return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[0] == '10000':
         # {"feature": "C_104320", "instances": 99, "metric_value": 19.4995, "depth": 3}
         if obj[17]<=222.33333333333334:
            # {"feature": "C_906370", "instances": 50, "metric_value": 13.5846, "depth": 4}
            if obj[33]<=4.0:
               # {"feature": "C_600160", "instances": 26, "metric_value": 9.4373, "depth": 5}
               if obj[42]<=44.0:
                  return 'G'
               elif obj[42]>44.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[33]>4.0:
               return 'G'
            else:
               return 'G'
         elif obj[17]>222.33333333333334:
            return 'G'
         else:
            return 'G'
      else:
         return 'G'
   elif obj[1] == '10100':
      # {"feature": "C_600570", "instances": 2506, "metric_value": 109.5181, "depth": 2}
      if obj[0] == '10100':
         # {"feature": "C_107480", "instances": 1459, "metric_value": 72.0251, "depth": 3}
         if obj[31]<=31.880945853324196:
            # {"feature": "C_116000", "instances": 769, "metric_value": 50.8475, "depth": 4}
            if obj[45]<=2.0:
               # {"feature": "C_752400", "instances": 409, "metric_value": 36.489, "depth": 5}
               if obj[23]>1.0:
                  return 'G'
               elif obj[23]<=1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[45]>2.0:
               # {"feature": "C_100000", "instances": 360, "metric_value": 35.4349, "depth": 5}
               if obj[18]<=6.0:
                  return 'G'
               elif obj[18]>6.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[31]>31.880945853324196:
            # {"feature": "C_100110", "instances": 690, "metric_value": 51.0129, "depth": 4}
            if obj[13]<=1.0:
               # {"feature": "C_906370", "instances": 346, "metric_value": 36.1267, "depth": 5}
               if obj[33]>5.638728323699422:
                  return 'G'
               elif obj[33]<=5.638728323699422:
                  return 'G'
               else:
                  return 'G'
            elif obj[13]>1.0:
               # {"feature": "C_106600", "instances": 344, "metric_value": 36.0249, "depth": 5}
               if obj[37]>0.0:
                  return 'G'
               elif obj[37]<=0.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[0] == '10000':
         # {"feature": "C_107480", "instances": 498, "metric_value": 41.9528, "depth": 3}
         if obj[31]<=38.76044176706827:
            # {"feature": "C_750100", "instances": 268, "metric_value": 30.0528, "depth": 4}
            if obj[19]>1.0:
               # {"feature": "C_114100", "instances": 138, "metric_value": 21.5221, "depth": 5}
               if obj[41]>0.759527536231884:
                  return 'G'
               elif obj[41]<=0.759527536231884:
                  return 'G'
               else:
                  return 'G'
            elif obj[19]<=1.0:
               # {"feature": "C_750300", "instances": 130, "metric_value": 21.0692, "depth": 5}
               if obj[20]>1.0:
                  return 'G'
               elif obj[20]<=1.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[31]>38.76044176706827:
            # {"feature": "C_106600", "instances": 230, "metric_value": 29.2805, "depth": 4}
            if obj[37]>0.0:
               # {"feature": "C_106880", "instances": 118, "metric_value": 20.6235, "depth": 5}
               if obj[10]>2.0:
                  return 'G'
               elif obj[10]<=2.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[37]<=0.0:
               # {"feature": "C_100120", "instances": 112, "metric_value": 20.7581, "depth": 5}
               if obj[14]>2.0:
                  return 'G'
               elif obj[14]<=2.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[0] == '00100':
         # {"feature": "C_100120", "instances": 422, "metric_value": 38.9505, "depth": 3}
         if obj[14]<=1.0:
            # {"feature": "C_107480", "instances": 215, "metric_value": 27.1475, "depth": 4}
            if obj[31]>43.47441860465116:
               # {"feature": "C_106880", "instances": 111, "metric_value": 19.1893, "depth": 5}
               if obj[10]<=1.0:
                  return 'G'
               elif obj[10]>1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[31]<=43.47441860465116:
               # {"feature": "C_906370", "instances": 104, "metric_value": 19.223, "depth": 5}
               if obj[33]>4.0:
                  return 'G'
               elif obj[33]<=4.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[14]>1.0:
            # {"feature": "C_906370", "instances": 207, "metric_value": 27.9402, "depth": 4}
            if obj[33]<=3.0:
               # {"feature": "C_750100", "instances": 104, "metric_value": 20.0062, "depth": 5}
               if obj[19]>1.0:
                  return 'G'
               elif obj[19]<=1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[33]>3.0:
               # {"feature": "C_107480", "instances": 103, "metric_value": 19.5224, "depth": 5}
               if obj[31]>40.24951456310679:
                  return 'G'
               elif obj[31]<=40.24951456310679:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[0] == '00000':
         return 'G'
      else:
         return 'G'
   elif obj[1] == '11110':
      # {"feature": "C_600570", "instances": 1955, "metric_value": 187.5838, "depth": 2}
      if obj[0] == '11110':
         # {"feature": "C_100120", "instances": 700, "metric_value": 52.7621, "depth": 3}
         if obj[14]<=3.0:
            # {"feature": "C_906370", "instances": 358, "metric_value": 37.6308, "depth": 4}
            if obj[33]>11.918994413407821:
               # {"feature": "C_106880", "instances": 180, "metric_value": 26.5363, "depth": 5}
               if obj[10]>1.0:
                  return 'G'
               elif obj[10]<=1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[33]<=11.918994413407821:
               return 'G'
            else:
               return 'G'
         elif obj[14]>3.0:
            return 'G'
         else:
            return 'G'
      elif obj[0] == '11010':
         # {"feature": "C_100000", "instances": 465, "metric_value": 42.9405, "depth": 3}
         if obj[18]>7.0:
            # {"feature": "C_100120", "instances": 239, "metric_value": 30.6599, "depth": 4}
            if obj[14]>5.0:
               return 'G'
            elif obj[14]<=5.0:
               # {"feature": "C_104320", "instances": 119, "metric_value": 21.4521, "depth": 5}
               if obj[17]>161.14285714285714:
                  return 'G'
               elif obj[17]<=161.14285714285714:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[18]<=7.0:
            return 'G'
         else:
            return 'G'
      elif obj[0] == '01110':
         return 'G'
      elif obj[0] == '01010':
         return 'G'
      elif obj[0] == '11100':
         return 'G'
      elif obj[0] == '01100':
         return 'G'
      elif obj[0] == '10110':
         return 'G'
      elif obj[0] == '11000':
         return 'G'
      elif obj[0] == '01000':
         return 'G'
      elif obj[0] == '00110':
         return 'G'
      elif obj[0] == '10010':
         return 'G'
      elif obj[0] == '00010':
         return 'G'
      elif obj[0] == '10100':
         return 'G'
      elif obj[0] == '10000':
         return 'G'
      elif obj[0] == '00100':
         return 'G'
      else:
         return 'G'
   elif obj[1] == '00010':
      # {"feature": "C_961223", "instances": 1634, "metric_value": 78.9395, "depth": 2}
      if obj[43]>-390.68591187270505:
         # {"feature": "C_999032", "instances": 846, "metric_value": 57.3293, "depth": 3}
         if obj[35]>0.0:
            # {"feature": "C_990660", "instances": 458, "metric_value": 41.6803, "depth": 4}
            if obj[46]>-56.18465065502184:
               # {"feature": "C_906370", "instances": 230, "metric_value": 29.5413, "depth": 5}
               if obj[33]>0.0:
                  return 'G'
               elif obj[33]<=0.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[46]<=-56.18465065502184:
               # {"feature": "C_111500", "instances": 228, "metric_value": 29.3666, "depth": 5}
               if obj[24]<=-1.0:
                  return 'G'
               elif obj[24]>-1.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[35]<=0.0:
            return 'G'
         else:
            return 'G'
      elif obj[43]<=-390.68591187270505:
         # {"feature": "C_106800", "instances": 788, "metric_value": 54.2882, "depth": 3}
         if obj[29]<=0.0:
            # {"feature": "C_116000", "instances": 395, "metric_value": 39.4826, "depth": 4}
            if obj[45]<=0.0:
               # {"feature": "C_752400", "instances": 222, "metric_value": 29.532, "depth": 5}
               if obj[23]<=0.0:
                  return 'G'
               elif obj[23]>0.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[45]>0.0:
               return 'G'
            else:
               return 'G'
         elif obj[29]>0.0:
            # {"feature": "C_990660", "instances": 393, "metric_value": 37.1625, "depth": 4}
            if obj[46]<=-1000.0:
               # {"feature": "C_104320", "instances": 214, "metric_value": 27.884, "depth": 5}
               if obj[17]<=6.0:
                  return 'G'
               elif obj[17]>6.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[46]>-1000.0:
               # {"feature": "C_111620", "instances": 179, "metric_value": 24.6766, "depth": 5}
               if obj[6]>-1.0:
                  return 'G'
               elif obj[6]<=-1.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      else:
         return 'G'
   elif obj[1] == '10110':
      # {"feature": "C_600570", "instances": 1443, "metric_value": 117.7429, "depth": 2}
      if obj[0] == '10110':
         # {"feature": "C_114100", "instances": 710, "metric_value": 52.3864, "depth": 3}
         if obj[41]>0.6821681690140845:
            # {"feature": "C_100120", "instances": 381, "metric_value": 37.8263, "depth": 4}
            if obj[14]<=4.981627296587926:
               # {"feature": "C_110720", "instances": 200, "metric_value": 26.5268, "depth": 5}
               if obj[32]<=8.445:
                  return 'G'
               elif obj[32]>8.445:
                  return 'G'
               else:
                  return 'G'
            elif obj[14]>4.981627296587926:
               return 'G'
            else:
               return 'G'
         elif obj[41]<=0.6821681690140845:
            return 'G'
         else:
            return 'G'
      elif obj[0] == '10010':
         # {"feature": "C_110720", "instances": 295, "metric_value": 33.1984, "depth": 3}
         if obj[32]<=10.159322033898306:
            # {"feature": "C_106880", "instances": 162, "metric_value": 23.8854, "depth": 4}
            if obj[10]<=2.0:
               # {"feature": "C_114100", "instances": 91, "metric_value": 17.4594, "depth": 5}
               if obj[41]>0.6528494505494505:
                  return 'G'
               elif obj[41]<=0.6528494505494505:
                  return 'G'
               else:
                  return 'G'
            elif obj[10]>2.0:
               # {"feature": "C_906370", "instances": 71, "metric_value": 16.3835, "depth": 5}
               if obj[33]<=11.32394366197183:
                  return 'G'
               elif obj[33]>11.32394366197183:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[32]>10.159322033898306:
            return 'G'
         else:
            return 'G'
      elif obj[0] == '00110':
         # {"feature": "C_114100", "instances": 216, "metric_value": 29.1216, "depth": 3}
         if obj[41]>0.5822921296296296:
            # {"feature": "C_100110", "instances": 112, "metric_value": 20.7905, "depth": 4}
            if obj[13]>1.0:
               # {"feature": "C_110720", "instances": 57, "metric_value": 14.578, "depth": 5}
               if obj[32]>7.0:
                  return 'G'
               elif obj[32]<=7.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[13]<=1.0:
               return 'G'
            else:
               return 'G'
         elif obj[41]<=0.5822921296296296:
            return 'G'
         else:
            return 'G'
      elif obj[0] == '00010':
         # {"feature": "C_906370", "instances": 85, "metric_value": 17.5878, "depth": 3}
         if obj[33]>0.0:
            # {"feature": "C_107480", "instances": 45, "metric_value": 12.2661, "depth": 4}
            if obj[31]<=65.1711111111111:
               # {"feature": "C_106880", "instances": 26, "metric_value": 8.7148, "depth": 5}
               if obj[10]<=2.0:
                  return 'G'
               elif obj[10]>2.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[31]>65.1711111111111:
               return 'G'
            else:
               return 'G'
         elif obj[33]<=0.0:
            return 'G'
         else:
            return 'G'
      elif obj[0] == '10100':
         # {"feature": "C_502400", "instances": 71, "metric_value": 15.7677, "depth": 3}
         if obj[5] == 'G':
            # {"feature": "C_116000", "instances": 63, "metric_value": 14.4124, "depth": 4}
            if obj[45]>2.0:
               # {"feature": "C_100120", "instances": 38, "metric_value": 10.4903, "depth": 5}
               if obj[14]<=8.0:
                  return 'G'
               elif obj[14]>8.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[45]<=2.0:
               return 'G'
            else:
               return 'G'
         elif obj[5] == 'B':
            return 'G'
         elif obj[5] == 'I':
            return 'G'
         else:
            return 'G'
      elif obj[0] == '10000':
         # {"feature": "C_107480", "instances": 39, "metric_value": 10.6699, "depth": 3}
         if obj[31]<=49.77179487179486:
            # {"feature": "C_104320", "instances": 23, "metric_value": 7.2863, "depth": 4}
            if obj[17]<=79.0:
               # {"feature": "C_114100", "instances": 15, "metric_value": 6.3146, "depth": 5}
               if obj[41]<=0.9504:
                  return 'G'
               elif obj[41]>0.9504:
                  return 'B'
               else:
                  return 'G'
            elif obj[17]>79.0:
               return 'G'
            else:
               return 'G'
         elif obj[31]>49.77179487179486:
            return 'G'
         else:
            return 'G'
      elif obj[0] == '00100':
         return 'G'
      else:
         return 'G'
   elif obj[1] == '11100':
      # {"feature": "C_600570", "instances": 1428, "metric_value": 119.2258, "depth": 2}
      if obj[0] == '11100':
         # {"feature": "C_906370", "instances": 628, "metric_value": 49.7993, "depth": 3}
         if obj[33]>11.584394904458598:
            return 'G'
         elif obj[33]<=11.584394904458598:
            # {"feature": "C_114100", "instances": 312, "metric_value": 34.8763, "depth": 4}
            if obj[41]>0.6344724358974358:
               # {"feature": "C_102800", "instances": 158, "metric_value": 24.5091, "depth": 5}
               if obj[28]>16.67:
                  return 'G'
               elif obj[28]<=16.67:
                  return 'G'
               else:
                  return 'G'
            elif obj[41]<=0.6344724358974358:
               return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[0] == '11000':
         # {"feature": "C_906370", "instances": 344, "metric_value": 36.8788, "depth": 3}
         if obj[33]<=9.270348837209303:
            # {"feature": "C_100000", "instances": 176, "metric_value": 26.2315, "depth": 4}
            if obj[18]>5.0:
               return 'G'
            elif obj[18]<=5.0:
               # {"feature": "C_750100", "instances": 88, "metric_value": 18.3398, "depth": 5}
               if obj[19]<=1.0:
                  return 'G'
               elif obj[19]>1.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[33]>9.270348837209303:
            return 'G'
         else:
            return 'G'
      elif obj[0] == '01100':
         # {"feature": "C_100000", "instances": 257, "metric_value": 31.8109, "depth": 3}
         if obj[18]<=4.0:
            return 'G'
         elif obj[18]>4.0:
            # {"feature": "C_100100", "instances": 127, "metric_value": 22.1863, "depth": 4}
            if obj[12]<=1.0:
               # {"feature": "C_100110", "instances": 66, "metric_value": 15.7625, "depth": 5}
               if obj[13]<=2.0:
                  return 'G'
               elif obj[13]>2.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[12]>1.0:
               return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[0] == '01000':
         return 'G'
      elif obj[0] == '10100':
         return 'G'
      elif obj[0] == '00100':
         return 'G'
      elif obj[0] == '10000':
         return 'G'
      else:
         return 'G'
   elif obj[1] == '00011':
      # {"feature": "C_100140", "instances": 1161, "metric_value": 59.3526, "depth": 2}
      if obj[15]<=1.0:
         # {"feature": "C_107480", "instances": 685, "metric_value": 42.0888, "depth": 3}
         if obj[31]<=58.33810218978103:
            # {"feature": "C_650640", "instances": 482, "metric_value": 32.4614, "depth": 4}
            if obj[25]<=678.9045643153527:
               # {"feature": "C_750600", "instances": 279, "metric_value": 23.7148, "depth": 5}
               if obj[21]>0.0:
                  return 'G'
               elif obj[21]<=0.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[25]>678.9045643153527:
               # {"feature": "C_111620", "instances": 203, "metric_value": 22.3495, "depth": 5}
               if obj[6]<=-1.0:
                  return 'G'
               elif obj[6]>-1.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[31]>58.33810218978103:
            # {"feature": "C_104320", "instances": 203, "metric_value": 27.1112, "depth": 4}
            if obj[17]<=151.73891625615764:
               # {"feature": "C_752400", "instances": 105, "metric_value": 18.5437, "depth": 5}
               if obj[23]>0.0:
                  return 'G'
               elif obj[23]<=0.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[17]>151.73891625615764:
               return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[15]>1.0:
         # {"feature": "C_106880", "instances": 476, "metric_value": 41.9848, "depth": 3}
         if obj[10]>0.0:
            # {"feature": "C_110720", "instances": 238, "metric_value": 29.5651, "depth": 4}
            if obj[32]<=0.0:
               # {"feature": "C_912070", "instances": 122, "metric_value": 20.6667, "depth": 5}
               if obj[34]<=0.0:
                  return 'G'
               elif obj[34]>0.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[32]>0.0:
               # {"feature": "C_100000", "instances": 116, "metric_value": 21.1504, "depth": 5}
               if obj[18]>2.0:
                  return 'G'
               elif obj[18]<=2.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[10]<=0.0:
            # {"feature": "C_104320", "instances": 238, "metric_value": 29.8236, "depth": 4}
            if obj[17]<=134.3403361344538:
               # {"feature": "C_906370", "instances": 132, "metric_value": 21.6217, "depth": 5}
               if obj[33]<=1.0:
                  return 'G'
               elif obj[33]>1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[17]>134.3403361344538:
               return 'G'
            else:
               return 'G'
         else:
            return 'G'
      else:
         return 'G'
   elif obj[1] == '01010':
      # {"feature": "C_600570", "instances": 1064, "metric_value": 70.0833, "depth": 2}
      if obj[0] == '01010':
         # {"feature": "C_111640", "instances": 825, "metric_value": 57.3064, "depth": 3}
         if obj[7]<=-1.0:
            # {"feature": "C_906370", "instances": 416, "metric_value": 40.596, "depth": 4}
            if obj[33]<=5.0:
               # {"feature": "C_104320", "instances": 212, "metric_value": 28.8467, "depth": 5}
               if obj[17]>152.93867924528303:
                  return 'G'
               elif obj[17]<=152.93867924528303:
                  return 'G'
               else:
                  return 'G'
            elif obj[33]>5.0:
               return 'G'
            else:
               return 'G'
         elif obj[7]>-1.0:
            return 'G'
         else:
            return 'G'
      elif obj[0] == '01000':
         return 'G'
      elif obj[0] == '00010':
         return 'G'
      else:
         return 'G'
   elif obj[1] == '01000':
      # {"feature": "C_752400", "instances": 1041, "metric_value": 63.8825, "depth": 2}
      if obj[23]>0.0:
         # {"feature": "C_111500", "instances": 552, "metric_value": 46.4809, "depth": 3}
         if obj[24]>-1.0:
            # {"feature": "C_750600", "instances": 284, "metric_value": 32.9981, "depth": 4}
            if obj[21]<=1.0:
               # {"feature": "C_750100", "instances": 145, "metric_value": 23.0886, "depth": 5}
               if obj[19]<=0.0:
                  return 'G'
               elif obj[19]>0.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[21]>1.0:
               return 'G'
            else:
               return 'G'
         elif obj[24]<=-1.0:
            return 'G'
         else:
            return 'G'
      elif obj[23]<=0.0:
         # {"feature": "C_906370", "instances": 489, "metric_value": 43.8649, "depth": 3}
         if obj[33]<=1.0:
            # {"feature": "C_114900", "instances": 245, "metric_value": 31.026, "depth": 4}
            if obj[49]>329.31836734693877:
               # {"feature": "C_114100", "instances": 134, "metric_value": 22.5567, "depth": 5}
               if obj[41]>0.8411238805970149:
                  return 'G'
               elif obj[41]<=0.8411238805970149:
                  return 'G'
               else:
                  return 'G'
            elif obj[49]<=329.31836734693877:
               return 'G'
            else:
               return 'G'
         elif obj[33]>1.0:
            # {"feature": "C_990660", "instances": 244, "metric_value": 30.9794, "depth": 4}
            if obj[46]<=-384.0187704918033:
               return 'G'
            elif obj[46]>-384.0187704918033:
               # {"feature": "C_930623", "instances": 119, "metric_value": 21.3473, "depth": 5}
               if obj[27]<=-0.5368907563025209:
                  return 'G'
               elif obj[27]>-0.5368907563025209:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         else:
            return 'G'
      else:
         return 'G'
   elif obj[1] == '00100':
      # {"feature": "C_104320", "instances": 841, "metric_value": 55.0099, "depth": 2}
      if obj[17]<=40.715814506539836:
         # {"feature": "C_107480", "instances": 458, "metric_value": 39.1095, "depth": 3}
         if obj[31]<=20.074454148471617:
            # {"feature": "C_114900", "instances": 251, "metric_value": 27.6442, "depth": 4}
            if obj[49]<=54.54183266932271:
               # {"feature": "C_906370", "instances": 126, "metric_value": 20.3195, "depth": 5}
               if obj[33]>4.0:
                  return 'G'
               elif obj[33]<=4.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[49]>54.54183266932271:
               # {"feature": "C_750100", "instances": 125, "metric_value": 18.8519, "depth": 5}
               if obj[19]<=1.0:
                  return 'G'
               elif obj[19]>1.0:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[31]>20.074454148471617:
            # {"feature": "C_114900", "instances": 207, "metric_value": 27.6803, "depth": 4}
            if obj[49]>45.56521739130435:
               # {"feature": "C_114100", "instances": 113, "metric_value": 19.7982, "depth": 5}
               if obj[41]>0.6280628318584071:
                  return 'G'
               elif obj[41]<=0.6280628318584071:
                  return 'G'
               else:
                  return 'G'
            elif obj[49]<=45.56521739130435:
               return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[17]>40.715814506539836:
         # {"feature": "C_111600", "instances": 383, "metric_value": 38.7261, "depth": 3}
         if obj[48]>-1.0:
            # {"feature": "C_906370", "instances": 203, "metric_value": 27.9318, "depth": 4}
            if obj[33]<=1.0:
               # {"feature": "C_750100", "instances": 104, "metric_value": 20.003, "depth": 5}
               if obj[19]>0.0:
                  return 'G'
               elif obj[19]<=0.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[33]>1.0:
               # {"feature": "C_114100", "instances": 99, "metric_value": 19.4988, "depth": 5}
               if obj[41]>0.7962828282828283:
                  return 'G'
               elif obj[41]<=0.7962828282828283:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[48]<=-1.0:
            return 'G'
         else:
            return 'G'
      else:
         return 'G'
   elif obj[1] == '01011':
      # {"feature": "C_600570", "instances": 807, "metric_value": 77.7154, "depth": 2}
      if obj[0] == '01011':
         # {"feature": "C_107480", "instances": 527, "metric_value": 45.5584, "depth": 3}
         if obj[31]>133.33662239089182:
            # {"feature": "C_906370", "instances": 272, "metric_value": 32.7423, "depth": 4}
            if obj[33]>1.0:
               return 'G'
            elif obj[33]<=1.0:
               # {"feature": "C_102800", "instances": 136, "metric_value": 22.9825, "depth": 5}
               if obj[28]<=33.33:
                  return 'G'
               elif obj[28]>33.33:
                  return 'G'
               else:
                  return 'G'
            else:
               return 'G'
         elif obj[31]<=133.33662239089182:
            # {"feature": "C_110720", "instances": 255, "metric_value": 31.6827, "depth": 4}
            if obj[32]>0.0:
               # {"feature": "C_114100", "instances": 134, "metric_value": 22.8029, "depth": 5}
               if obj[41]<=0.909368656716418:
                  return 'G'
               elif obj[41]>0.909368656716418:
                  return 'G'
               else:
                  return 'G'
            elif obj[32]<=0.0:
               return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[0] == '01000':
         return 'G'
      elif obj[0] == '01010':
         return 'G'
      elif obj[0] == '00011':
         return 'G'
      elif obj[0] == '00010':
         return 'G'
      elif obj[0] == '01001':
         return 'G'
      else:
         return 'G'
   elif obj[1] == '01110':
      # {"feature": "C_600570", "instances": 694, "metric_value": 80.9389, "depth": 2}
      if obj[0] == '01110':
         return 'G'
      elif obj[0] == '01010':
         # {"feature": "C_104320", "instances": 187, "metric_value": 27.0585, "depth": 3}
         if obj[17]>197.06951871657753:
            # {"feature": "C_110720", "instances": 95, "metric_value": 19.0871, "depth": 4}
            if obj[32]<=10.74736842105263:
               # {"feature": "C_100000", "instances": 49, "metric_value": 13.4374, "depth": 5}
               if obj[18]>3.0:
                  return 'G'
               elif obj[18]<=3.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[32]>10.74736842105263:
               return 'G'
            else:
               return 'G'
         elif obj[17]<=197.06951871657753:
            return 'G'
         else:
            return 'G'
      elif obj[0] == '01100':
         return 'G'
      elif obj[0] == '00110':
         return 'G'
      elif obj[0] == '01000':
         return 'G'
      elif obj[0] == '00010':
         return 'G'
      elif obj[0] == '00100':
         return 'G'
      else:
         return 'G'
   elif obj[1] == '01111':
      return 'G'
   elif obj[1] == '01100':
      # {"feature": "C_600570", "instances": 542, "metric_value": 50.0966, "depth": 2}
      if obj[0] == '01100':
         # {"feature": "C_104320", "instances": 363, "metric_value": 37.8852, "depth": 3}
         if obj[17]<=125.94490358126721:
            return 'G'
         elif obj[17]>125.94490358126721:
            # {"feature": "C_100000", "instances": 175, "metric_value": 26.1511, "depth": 4}
            if obj[18]<=3.0:
               # {"feature": "C_750100", "instances": 93, "metric_value": 18.8745, "depth": 5}
               if obj[19]<=1.0:
                  return 'G'
               elif obj[19]>1.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[18]>3.0:
               return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[0] == '01000':
         # {"feature": "C_111660", "instances": 138, "metric_value": 23.141, "depth": 3}
         if obj[8]<=-1.0:
            return 'G'
         elif obj[8]>-1.0:
            # {"feature": "C_111600", "instances": 66, "metric_value": 15.7611, "depth": 4}
            if obj[48]>-1.0:
               # {"feature": "C_906370", "instances": 34, "metric_value": 10.9928, "depth": 5}
               if obj[33]>0.0:
                  return 'G'
               elif obj[33]<=0.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[48]<=-1.0:
               return 'G'
            else:
               return 'G'
         else:
            return 'G'
      elif obj[0] == '00100':
         return 'G'
      else:
         return 'G'
   elif obj[1] == '00110':
      # {"feature": "C_600570", "instances": 423, "metric_value": 44.2351, "depth": 2}
      if obj[0] == '00110':
         # {"feature": "C_114900", "instances": 291, "metric_value": 33.8833, "depth": 3}
         if obj[49]>58.824742268041234:
            # {"feature": "C_100000", "instances": 149, "metric_value": 24.0864, "depth": 4}
            if obj[18]>2.0:
               # {"feature": "C_906370", "instances": 75, "metric_value": 16.8641, "depth": 5}
               if obj[33]>5.0:
                  return 'G'
               elif obj[33]<=5.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[18]<=2.0:
               return 'G'
            else:
               return 'G'
         elif obj[49]<=58.824742268041234:
            return 'G'
         else:
            return 'G'
      elif obj[0] == '00010':
         # {"feature": "C_107480", "instances": 95, "metric_value": 19.0843, "depth": 3}
         if obj[31]<=99.21368421052631:
            # {"feature": "C_111640", "instances": 51, "metric_value": 13.7323, "depth": 4}
            if obj[7]<=-1.0:
               # {"feature": "C_104320", "instances": 27, "metric_value": 9.6459, "depth": 5}
               if obj[17]<=70.77777777777777:
                  return 'G'
               elif obj[17]>70.77777777777777:
                  return 'G'
               else:
                  return 'G'
            elif obj[7]>-1.0:
               return 'G'
            else:
               return 'G'
         elif obj[31]>99.21368421052631:
            return 'G'
         else:
            return 'G'
      elif obj[0] == '00100':
         return 'G'
      else:
         return 'G'
   elif obj[1] == '00111':
      # {"feature": "C_600570", "instances": 393, "metric_value": 56.203, "depth": 2}
      if obj[0] == '00111':
         # {"feature": "C_107480", "instances": 200, "metric_value": 26.8919, "depth": 3}
         if obj[31]<=88.6865:
            # {"feature": "C_104320", "instances": 104, "metric_value": 18.4661, "depth": 4}
            if obj[17]<=94.32692307692308:
               # {"feature": "C_106800", "instances": 66, "metric_value": 13.8329, "depth": 5}
               if obj[29]>0.0:
                  return 'G'
               elif obj[29]<=0.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[17]>94.32692307692308:
               return 'G'
            else:
               return 'G'
         elif obj[31]>88.6865:
            return 'G'
         else:
            return 'G'
      elif obj[0] == '00011':
         # {"feature": "C_750100", "instances": 69, "metric_value": 16.1379, "depth": 3}
         if obj[19]>1.0:
            # {"feature": "C_110720", "instances": 36, "metric_value": 11.349, "depth": 4}
            if obj[32]<=5.0:
               # {"feature": "C_104320", "instances": 20, "metric_value": 8.0825, "depth": 5}
               if obj[17]<=180.0:
                  return 'G'
               elif obj[17]>180.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[32]>5.0:
               return 'G'
            else:
               return 'G'
         elif obj[19]<=1.0:
            return 'G'
         else:
            return 'G'
      elif obj[0] == '00100':
         # {"feature": "C_100110", "instances": 54, "metric_value": 13.6414, "depth": 3}
         if obj[13]<=1.0:
            # {"feature": "C_107480", "instances": 30, "metric_value": 9.5656, "depth": 4}
            if obj[31]<=43.906666666666666:
               # {"feature": "C_650640", "instances": 18, "metric_value": 6.7301, "depth": 5}
               if obj[25]<=1344.0:
                  return 'G'
               elif obj[25]>1344.0:
                  return 'G'
               else:
                  return 'G'
            elif obj[31]>43.906666666666666:
               return 'G'
            else:
               return 'G'
         elif obj[13]>1.0:
            return 'G'
         else:
            return 'G'
      elif obj[0] == '00110':
         return 'G'
      elif obj[0] == '00010':
         return 'G'
      elif obj[0] == '00101':
         return 'G'
      elif obj[0] == '00001':
         return 'G'
      else:
         return 'G'
   elif obj[1] == '10101':
      return 'G'
   elif obj[1] == '11101':
      return 'G'
   elif obj[1] == '10001':
      # {"feature": "C_600570", "instances": 136, "metric_value": 24.9878, "depth": 2}
      if obj[0] == '10001':
         return 'G'
      elif obj[0] == '10000':
         # {"feature": "C_104320", "instances": 25, "metric_value": 9.226, "depth": 3}
         if obj[17]>65.0:
            # {"feature": "C_501200", "instances": 14, "metric_value": 6.9109, "depth": 4}
            if obj[4] == 'G':
               # {"feature": "C_105740", "instances": 12, "metric_value": 6.1046, "depth": 5}
               if obj[44]>24.0:
                  return 'G'
               elif obj[44]<=24.0:
                  return 'B'
               else:
                  return 'G'
            elif obj[4] == 'I':
               return 'G'
            elif obj[4] == 'B':
               return 'G'
            else:
               return 'G'
         elif obj[17]<=65.0:
            return 'G'
         else:
            return 'G'
      elif obj[0] == '00001':
         return 'G'
      else:
         return 'G'
   elif obj[1] == '11001':
      return 'G'
   elif obj[1] == '00101':
      # {"feature": "C_600570", "instances": 54, "metric_value": 16.4018, "depth": 2}
      if obj[0] == '00101':
         # {"feature": "C_114100", "instances": 34, "metric_value": 10.9928, "depth": 3}
         if obj[41]>0.46566176470588233:
            # {"feature": "C_106860", "instances": 19, "metric_value": 7.8376, "depth": 4}
            if obj[9]<=2.0:
               # {"feature": "C_106880", "instances": 11, "metric_value": 5.8863, "depth": 5}
               if obj[10]<=2.0:
                  return 'G'
               elif obj[10]>2.0:
                  return 'B'
               else:
                  return 'G'
            elif obj[9]>2.0:
               return 'G'
            else:
               return 'G'
         elif obj[41]<=0.46566176470588233:
            return 'G'
         else:
            return 'G'
      elif obj[0] == '00100':
         return 'G'
      elif obj[0] == '00001':
         return 'G'
      else:
         return 'G'
   elif obj[1] == '01101':
      return 'G'
   elif obj[1] == '00001':
      # {"feature": "C_104320", "instances": 30, "metric_value": 10.244, "depth": 2}
      if obj[17]>140.06666666666666:
         # {"feature": "C_650640", "instances": 17, "metric_value": 7.3194, "depth": 3}
         if obj[25]<=6400.0:
            # {"feature": "C_906170", "instances": 10, "metric_value": 5.6569, "depth": 4}
            if obj[26]<=2.0:
               return 'G'
            elif obj[26]>2.0:
               return 'B'
            else:
               return 'G'
         elif obj[25]>6400.0:
            return 'G'
         else:
            return 'G'
      elif obj[17]<=140.06666666666666:
         return 'G'
      else:
         return 'G'
   elif obj[1] == '01001':
      return 'G'
   elif obj[1] == '00000':
      # {"feature": "C_104320", "instances": 14, "metric_value": 6.5132, "depth": 2}
      if obj[17]<=31.0:
         return 'G'
      elif obj[17]>31.0:
         return 'B'
      else:
         return 'G'
   else:
      return 'G'
