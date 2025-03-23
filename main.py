import avto_info_mod

avto1 = avto_info_mod.avto_info('GM', 'Malibu', 'qora', 'avtomat', 2020, 40000)
avto_info_mod.info_print(avto1)

import avto_info_mod as aim

avto1 = aim.avto_info('GM', 'Malibu', 'qora', 'avtomat', 2020, 40000)
avto_info_mod.info_print(avto1)

from avto_info_mod import info_print, avto_info

avto1 = avto_info('GM', 'Malibu', 'qora', 'avtomat', 2020, 40000)
info_print(avto1)

from avto_info_mod import avto_info as ainfo, info_print as inprint

avto1 = ainfo('GM', 'Malibu', 'qora', 'avtomat', 2020, 40000)
inprint(avto1)

