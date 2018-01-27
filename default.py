# -*- coding: utf-8 -*-
#------------------------------------------------------------
# jami
#------------------------------------------------------------
# Licença: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Baseado no código do addon youtube
#------------------------------------------------------------

import xbmc, xbmcaddon, xbmcplugin, os, sys, plugintools
from addon.common.addon import Addon

addonID = 'plugin.video.followmy'
addon   = Addon(addonID, sys.argv)
local   = xbmcaddon.Addon(id=addonID)
icon    = local.getAddonInfo('icon')
base    = 'plugin://plugin.video.youtube/'

fan01 = 'http://www.tudocelular.com/img/id132893.jpg'
icon01 = 'https://yt3.ggpht.com/-ZTRE_iLvZps/AAAAAAAAAAI/AAAAAAAAAAA/2Rre1C1ccZw/s176-c-k-no-mo-rj-c0xffffff/photo.jpg'
icon02 = 'https://yt3.ggpht.com/-NanHHMT55m8/AAAAAAAAAAI/AAAAAAAAAAA/MJrsWW5mY7I/s176-c-k-no-mo-rj-c0xffffff/photo.jpg'
icon02a = 'https://yt3.ggpht.com/-zlw8fIPyphY/AAAAAAAAAAI/AAAAAAAAAAA/tz_V59gT7H8/s176-c-k-no-mo-rj-c0xffffff/photo.jpg'
icon02b = 'https://yt3.ggpht.com/-4s4YJDVkU5A/AAAAAAAAAAI/AAAAAAAAAAA/8EJxqJO566w/s176-c-k-no-mo-rj-c0xffffff/photo.jpg'
icon02c = 'https://yt3.ggpht.com/-m6w1N2CG5G8/AAAAAAAAAAI/AAAAAAAAAAA/PKWSy9Tlvqw/s176-c-k-no-mo-rj-c0xffffff/photo.jpg'
icon02d = 'https://yt3.ggpht.com/-DAPGG6vCVxM/AAAAAAAAAAI/AAAAAAAAAAA/9ZaCa8RCAv8/s176-c-k-no-mo-rj-c0xffffff/photo.jpg'
icon03 = 'https://yt3.ggpht.com/-0tZI_ubklSA/AAAAAAAAAAI/AAAAAAAAAAA/tcrS8LB7xBA/s176-c-k-no-mo-rj-c0xffffff/photo.jpg'
icon04 = 'https://yt3.ggpht.com/-Yf2NShe4TXY/AAAAAAAAAAI/AAAAAAAAAAA/RM1rmSRBmbM/s176-c-k-no-mo-rj-c0xffffff/photo.jpg'
icon05 = 'https://yt3.ggpht.com/-0Qbr5BhIKPM/AAAAAAAAAAI/AAAAAAAAAAA/hXTf-fihSdo/s176-c-k-no-mo-rj-c0xffffff/photo.jpg'
icon06 = 'https://yt3.ggpht.com/-Fl5sOlzKGTQ/AAAAAAAAAAI/AAAAAAAAAAA/lF0YV6h2bdk/s176-c-k-no-mo-rj-c0xffffff/photo.jpg'
icon06a = 'https://yt3.ggpht.com/-zuhi9AuOr5A/AAAAAAAAAAI/AAAAAAAAAAA/2IYLP8Cg_W0/s176-c-k-no-mo-rj-c0xffffff/photo.jpg'
icon06b = 'https://yt3.ggpht.com/-cPZXEbiHsNc/AAAAAAAAAAI/AAAAAAAAAAA/s9_Oq4ve0cw/s176-c-k-no-mo-rj-c0xffffff/photo.jpg'
icon06c = 'https://yt3.ggpht.com/-QCzBhdBszlM/AAAAAAAAAAI/AAAAAAAAAAA/dpu5BOKsUJk/s176-c-k-no-mo-rj-c0xffffff/photo.jpg'
icon06d = 'https://yt3.ggpht.com/-_dNpZc9mBo8/AAAAAAAAAAI/AAAAAAAAAAA/OEXkG2N7-eI/s176-c-k-no-mo-rj-c0xffffff/photo.jpg'
icon07 = 'https://yt3.ggpht.com/-9u7FSwTiY7A/AAAAAAAAAAI/AAAAAAAAAAA/XwV33l1bDGo/s176-c-k-no-mo-rj-c0xffffff/photo.jpg'
icon08 = 'https://yt3.ggpht.com/-xle954Zxs4E/AAAAAAAAAAI/AAAAAAAAAAA/geYaRfTQ0FY/s176-c-k-no-mo-rj-c0xffffff/photo.jpg'
icon09 = 'https://yt3.ggpht.com/-3CBRGAWqlro/AAAAAAAAAAI/AAAAAAAAAAA/FScgKpEd8YQ/s176-c-k-no-mo-rj-c0xffffff/photo.jpg'
icon09a = 'https://i.ytimg.com/vi/o9bzRKI86YY/hqdefault.jpg'
icon09b = 'https://yt3.ggpht.com/-Tu9-5CljkIc/AAAAAAAAAAI/AAAAAAAAAAA/mlnaJsR73bc/s176-c-k-no-mo-rj-c0xffffff/photo.jpg'
icon09c = 'https://yt3.ggpht.com/-_8wmP1DT6Jw/AAAAAAAAAAI/AAAAAAAAAAA/Jx-XAdb7IXM/s176-c-k-no-mo-rj-c0xffffff/photo.jpg'
icon10 = 'https://yt3.ggpht.com/-Q0PO0xGoqmU/AAAAAAAAAAI/AAAAAAAAAAA/FfzSou2NY4A/s176-c-k-no-mo-rj-c0xffffff/photo.jpg'
icon11 = 'https://yt3.ggpht.com/-aV9DSpyoY00/AAAAAAAAAAI/AAAAAAAAAAA/4AT5XyMDUiQ/s176-c-k-no-mo-rj-c0xffffff/photo.jpg'
icon12 = 'https://yt3.ggpht.com/-ieZ9vYR36R0/AAAAAAAAAAI/AAAAAAAAAAA/8Xd9R-zTZ2g/s176-c-k-no-mo-rj-c0xffffff/photo.jpg'
icon13 = 'https://yt3.ggpht.com/-jvUnoRLOnX4/AAAAAAAAAAI/AAAAAAAAAAA/zTEuVrRTLsQ/s176-c-k-no-mo-rj-c0xffffff/photo.jpg'
icon14 = 'https://i.ytimg.com/vi/68dx-XdzjV4/hqdefault.jpg'
icon15 = 'https://i.ytimg.com/vi/4g2wxGF5hZ4/hqdefault.jpg'
icon16 = 'https://i.ytimg.com/vi/Gq3OA1lA1_E/hqdefault.jpg'
icon17 = 'https://yt3.ggpht.com/-fY199RcXnZ4/AAAAAAAAAAI/AAAAAAAAAAA/qMiFrTDiPsI/s176-c-k-no-mo-rj-c0xffffff/photo.jpg'
icon18 = 'https://yt3.ggpht.com/-l2VDs_YGTio/AAAAAAAAAAI/AAAAAAAAAAA/zanZbAKXVgQ/s176-c-k-no-mo-rj-c0xffffff/photo.jpg'
icon19 = 'https://yt3.ggpht.com/-9fVK_jlm9kg/AAAAAAAAAAI/AAAAAAAAAAA/Fe4GUv-0oE8/s176-c-k-no-mo-rj-c0xffffff/photo.jpg'
icon20 = 'https://yt3.ggpht.com/-udjsIr20KGU/AAAAAAAAAAI/AAAAAAAAAAA/w5XjvZ_6P3g/s176-c-k-no-mo-rj-c0xffffff/photo.jpg'
icon21 = 'https://yt3.ggpht.com/-bonZt347bMc/AAAAAAAAAAI/AAAAAAAAAAA/lR8QEKnqqHk/s176-c-k-no-mo-rj-c0xffffff/photo.jpg'
icon22 = 'https://thumbs.dreamstime.com/x/%C3%ADcone-para-o-dobrador-dos-favoritos-7692115.jpg'


def run():
    plugintools.log("FollowMy.run")
    params = plugintools.get_params()
    if params.get("action") is None: main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    plugintools.close_item_list()

def main_list(params):
	plugintools.log("FollowMy ===> " + repr(params))
	plugintools.add_item(title = "Olhar Digital Plus [BR]", url = base + "channel/UCYfawpzMYkxKcCDJMs5tWXg/", thumbnail = icon01, fanart = fan01, folder = True)
	plugintools.add_item(title = "Olhar Digital Diario [BR]", url = base + "channel/UCGV72aVJuWP0QPNGH4YgIww/", thumbnail = icon02, fanart = fan01, folder = True)	
	plugintools.add_item(title = "Manual do Mundo [BR]", url = base + "user/iberethenorio/", thumbnail = icon02a, fanart = fan01, folder = True)
	plugintools.add_item(title = "elFuturoEsOne [ES]", url = base + "channel/UC_PZITA0uBZRC5E1fCrBVXQ/", thumbnail = icon02b, fanart = fan01, folder = True)	
	plugintools.add_item(title = "EL ANGELITO [ES]", url = base + "user/canalelangelito/", thumbnail = icon02c, fanart = fan01, folder = True)
	plugintools.add_item(title = "Terrazocultor jose manuel [ES]", url = base + "user/Terrazocultor/", thumbnail = icon02d, fanart = fan01, folder = True)
	plugintools.add_item(title = "Empoeirados [BR]", url = base + "user/canalempoeirados/", thumbnail = icon03, fanart = fan01, folder = True)
	plugintools.add_item(title = "Oficina de Casa [BR]", url = base + "user/OficinaDeCasaComBr/", thumbnail = icon04, fanart = fan01, folder = True)
	plugintools.add_item(title = "Marcenaria Amadora [BR]", url = base + "user/MarcenariaAmadora/", thumbnail = icon05, fanart = fan01, folder = True)
	plugintools.add_item(title = "Nuno Agonia [PT]", url = base + "user/seemeetube/" , thumbnail = icon06, fanart = fan01, folder = True)	
	plugintools.add_item(title = "Bernardo Almeida [PT]", url = base + "user/listareproducaolagos/" , thumbnail = icon06a, fanart = fan01, folder = True)	
	plugintools.add_item(title = "4gnews [PT]", url = base + "user/4gnews/" , thumbnail = icon06b, fanart = fan01, folder = True)	
	plugintools.add_item(title = "Roberto Jorge [PT]", url = base + "channel/UCKla8sNVBGbS9RdEIZmA1DQ/" , thumbnail = icon06c, fanart = fan01, folder = True)	
	plugintools.add_item(title = "Clipset [ES]", url = base + "user/clipsetvideo/", thumbnail = icon06d, fanart = fan01, folder = True)
	plugintools.add_item(title = "Rui Unas - Maluco Beleza [PT]", url = base + "playlist/PLRMvb4nSbcLhhGYe7Wydvd92WppA44cvj/", thumbnail = icon07, fanart = fan01, folder = True)
	plugintools.add_item(title = "Porta dos Fundos [BR]", url = base + "user/portadosfundos/", thumbnail = icon08, fanart = fan01, folder = True)
	plugintools.add_item(title = "Diogo Bataguas [PT]", url = base + "user/BataguasD/", thumbnail = icon09, fanart = fan01, folder = True)
	plugintools.add_item(title = "Fernando Rocha [PT]", url = base + "user/rooooooocha/", thumbnail = icon09a, fanart = fan01, folder = True)
	plugintools.add_item(title = "Môce dum Cabréste [PT]", url = base + "user/MoceDumCabreste/", thumbnail = icon09b, fanart = fan01, folder = True)
	plugintools.add_item(title = "Maurício Meirelles [BR]", url = base + "user/mauriciomeirelles/", thumbnail = icon09c, fanart = fan01, folder = True)
	plugintools.add_item(title = "Thiago Ventura [BR]", url = base + "user/thiagosouzapires/", thumbnail = icon10, fanart = fan01, folder = True)
	plugintools.add_item(title = "Canal Q [PT]", url = base + "user/CanalQ15/", thumbnail = icon11, fanart = fan01, folder = True)
	plugintools.add_item(title = "RedeTV [BR]", url = base + "channel/UCd7VVhgnd2eCv9JEghvR_1w/", thumbnail = icon12, fanart = fan01, folder = True)
	plugintools.add_item(title = "MixYouTube - SIC [PT]", url = base + "user/shoppingcomprasebay/", thumbnail = icon13, fanart = fan01, folder = True)
	plugintools.add_item(title = "CONTAS POUPANÇA [PT]", url = base + "playlist/PLvuSEdMrOiFHZFEz6q_yBHeydD4m3cV36/", thumbnail = icon14, fanart = fan01, folder = True)
	plugintools.add_item(title = "FUTURO HOJE [PT]", url = base + "playlist/PLvuSEdMrOiFGE72U1iZs3w4yjbAovxaZg/", thumbnail = icon15, fanart = fan01, folder = True)
	plugintools.add_item(title = "NEGÓCIOS DA SEMANA [PT]", url = base + "playlist/PLvuSEdMrOiFF4eRd2bVTd-dM00AXyWpic/", thumbnail = icon16, fanart = fan01, folder = True)
	plugintools.add_item(title = "Academia Lair Ribeiro [BR]", url = base + "user/academialairribeiro/", thumbnail = icon17, fanart = fan01, folder = True)	
	plugintools.add_item(title = "Dr Juliano Pimentel [BR]", url = base + "user/MedPiment/", thumbnail = icon18, fanart = fan01, folder = True)
	plugintools.add_item(title = "TED Brasil [BR]", url = base + "channel/UCLzbgTjj2HFh9_lPJzKnZMA/" , thumbnail = icon19, fanart = fan01, folder = True)	
	plugintools.add_item(title = "TED en Español [ES]", url = base + "channel/UCshVTOdmZLdLj8LTV1j_0uw/" , thumbnail = icon20, fanart = fan01, folder = True)	
	plugintools.add_item(title = "TED [EN]", url = base + "user/TEDtalksDirector/" , thumbnail = icon21, fanart = fan01, folder = True)
	plugintools.add_item(title = "Favoritos Mendel", url = base + "playlist/FLZduWJp1TaJ9MrNnPI0KpKA/", thumbnail = icon22, fanart = fan01, folder = True)
	
	xbmcplugin.setContent(int(sys.argv[1]), 'movies')
	xbmc.executebuiltin('Container.SetViewMode()')
	
run()
