#!/usr/bin/python
"""
color support for MPlot.

"""
import numpy as np

from matplotlib.colors import LinearSegmentedColormap
from matplotlib.cm import register_cmap


x11_colors = {'aliceblue': (240,248,255), 'antiquewhite': (250,235,215),
              'antiquewhite1': (255,239,219), 'antiquewhite2': (238,223,204),
              'antiquewhite3': (205,192,176), 'antiquewhite4': (139,131,120),
              'aquamarine': (127,255,212), 'aquamarine1': (127,255,212),
              'aquamarine2': (118,238,198), 'aquamarine3': (102,205,170),
              'aquamarine4': ( 69,139,116), 'azure': (240,255,255),
              'azure1': (240,255,255), 'azure2': (224,238,238),
              'azure3': (193,205,205), 'azure4': (131,139,139),
              'beige': (245,245,220), 'bisque': (255,228,196),
              'bisque1': (255,228,196), 'bisque2': (238,213,183),
              'bisque3': (205,183,158), 'bisque4': (139,125,107),
              'black': (  0,  0,  0), 'blanchedalmond': (255,235,205),
              'blue':  (  0,  0,255), 'blue1': (  0,  0,255),
              'blue2': (  0,  0,238), 'blue3': (  0,  0,205),
              'blue4': (  0,  0,139), 'blueviolet': (138, 43,226),
              'brown': (165, 42, 42), 'brown1': (255, 64, 64),
              'brown2': (238, 59, 59), 'brown3': (205, 51, 51),
              'brown4': (139, 35, 35), 'burlywood': (222,184,135),
              'burlywood1': (255,211,155), 'burlywood2': (238,197,145),
              'burlywood3': (205,170,125), 'burlywood4': (139,115, 85),
              'cadetblue': ( 95,158,160), 'cadetblue1': (152,245,255),
              'cadetblue2': (142,229,238), 'cadetblue3': (122,197,205),
              'cadetblue4': ( 83,134,139), 'chartreuse': (127,255,  0),
              'chartreuse1': (127,255,  0), 'chartreuse2': (118,238,  0),
              'chartreuse3': (102,205,  0), 'chartreuse4': ( 69,139,  0),
              'chocolate': (210,105, 30), 'chocolate1': (255,127, 36),
              'chocolate2': (238,118, 33), 'chocolate3': (205,102, 29),
              'chocolate4': (139, 69, 19), 'coral': (255,127, 80),
              'coral1': (255,114, 86), 'coral2': (238,106, 80),
              'coral3': (205, 91, 69), 'coral4': (139, 62, 47),
              'cornflowerblue': (100,149,237), 'cornsilk': (255,248,220),
              'cornsilk1': (255,248,220), 'cornsilk2': (238,232,205),
              'cornsilk3': (205,200,177), 'cornsilk4': (139,136,120),
              'cyan':  (  0,255,255), 'cyan1': (  0,255,255),
              'cyan2': (  0,238,238), 'cyan3': (  0,205,205),
              'cyan4': (  0,139,139), 'darkblue': (  0,  0,139),
              'darkcyan': (  0,139,139), 'darkgoldenrod': (184,134, 11),
              'darkgoldenrod1': (255,185, 15), 'darkgoldenrod2': (238,173, 14),
              'darkgoldenrod3': (205,149, 12), 'darkgoldenrod4': (139,101,  8),
              'darkgreen': (  0,100,  0), 'darkgrey': (169,169,169),
              'darkkhaki': (189,183,107), 'darkmagenta': (139,  0,139),
              'darkolivegreen': ( 85,107, 47), 'darkolivegreen1': (202,255,112),
              'darkolivegreen2': (188,238,104), 'darkolivegreen3': (162,205, 90),
              'darkolivegreen4': (110,139, 61), 'darkorange': (255,140,  0),
              'darkorange1': (255,127,  0), 'darkorange2': (238,118,  0),
              'darkorange3': (205,102,  0), 'darkorange4': (139, 69,  0),
              'darkorchid': (153, 50,204), 'darkorchid1': (191, 62,255),
              'darkorchid2': (178, 58,238), 'darkorchid3': (154, 50,205),
              'darkorchid4': (104, 34,139), 'darkred': (139,  0,  0),
              'darksalmon': (233,150,122), 'darkseagreen': (143,188,143),
              'darkseagreen1': (193,255,193), 'darkseagreen2': (180,238,180),
              'darkseagreen3': (155,205,155), 'darkseagreen4': (105,139,105),
              'darkslateblue': ( 72, 61,139), 'darkslategrey': ( 47, 79, 79),
              'darkslategrey1': (151,255,255), 'darkslategrey2': (141,238,238),
              'darkslategrey3': (121,205,205), 'darkslategrey4': ( 82,139,139),
              'darkturquoise': (  0,206,209), 'darkviolet': (148,  0,211),
              'deeppink': (255, 20,147), 'deeppink1': (255, 20,147),
              'deeppink2': (238, 18,137), 'deeppink3': (205, 16,118),
              'deeppink4': (139, 10, 80), 'deepskyblue': (  0,191,255),
              'deepskyblue1': (  0,191,255), 'deepskyblue2': (  0,178,238),
              'deepskyblue3': (  0,154,205), 'deepskyblue4': (  0,104,139),
              'dimgrey': (105,105,105), 'dodgerblue': ( 30,144,255),
              'dodgerblue1': ( 30,144,255), 'dodgerblue2': ( 28,134,238),
              'dodgerblue3': ( 24,116,205), 'dodgerblue4': ( 16, 78,139),
              'firebrick': (178, 34, 34), 'firebrick1': (255, 48, 48),
              'firebrick2': (238, 44, 44), 'firebrick3': (205, 38, 38),
              'firebrick4': (139, 26, 26), 'floralwhite': (255,250,240),
              'forestgreen': ( 34,139, 34), 'gainsboro': (220,220,220),
              'ghostwhite': (248,248,255), 'gold':  (255,215,  0),
              'gold1': (255,215,  0), 'gold2': (238,201,  0),
              'gold3': (205,173,  0), 'gold4': (139,117,  0),
              'goldenrod': (218,165, 32), 'goldenrod1': (255,193, 37),
              'goldenrod2': (238,180, 34), 'goldenrod3': (205,155, 29),
              'goldenrod4': (139,105, 20), 'green': (  0,255,  0),
              'green1': (  0,255,  0), 'green2': (  0,238,  0),
              'green3': (  0,205,  0), 'green4': (  0,139,  0),
              'greenyellow': (173,255, 47), 'grey':  (190,190,190),
              'grey0': (  0,  0,  0), 'grey1': (  3,  3,  3),
              'grey10': ( 26, 26, 26), 'grey100': (255,255,255),
              'grey11': ( 28, 28, 28), 'grey12': ( 31, 31, 31),
              'grey13': ( 33, 33, 33), 'grey14': ( 36, 36, 36),
              'grey15': ( 38, 38, 38), 'grey16': ( 41, 41, 41),
              'grey17': ( 43, 43, 43), 'grey18': ( 46, 46, 46),
              'grey19': ( 48, 48, 48), 'grey2': (  5,  5,  5),
              'grey20': ( 51, 51, 51), 'grey21': ( 54, 54, 54),
              'grey22': ( 56, 56, 56), 'grey23': ( 59, 59, 59),
              'grey24': ( 61, 61, 61), 'grey25': ( 64, 64, 64),
              'grey26': ( 66, 66, 66), 'grey27': ( 69, 69, 69),
              'grey28': ( 71, 71, 71), 'grey29': ( 74, 74, 74),
              'grey3': (  8,  8,  8), 'grey30': ( 77, 77, 77),
              'grey31': ( 79, 79, 79), 'grey32': ( 82, 82, 82),
              'grey33': ( 84, 84, 84), 'grey34': ( 87, 87, 87),
              'grey35': ( 89, 89, 89), 'grey36': ( 92, 92, 92),
              'grey37': ( 94, 94, 94), 'grey38': ( 97, 97, 97),
              'grey39': ( 99, 99, 99), 'grey4': ( 10, 10, 10),
              'grey40': (102,102,102), 'grey41': (105,105,105),
              'grey42': (107,107,107), 'grey43': (110,110,110),
              'grey44': (112,112,112), 'grey45': (115,115,115),
              'grey46': (117,117,117), 'grey47': (120,120,120),
              'grey48': (122,122,122), 'grey49': (125,125,125),
              'grey5': ( 13, 13, 13), 'grey50': (127,127,127),
              'grey51': (130,130,130), 'grey52': (133,133,133),
              'grey53': (135,135,135), 'grey54': (138,138,138),
              'grey55': (140,140,140), 'grey56': (143,143,143),
              'grey57': (145,145,145), 'grey58': (148,148,148),
              'grey59': (150,150,150), 'grey6': ( 15, 15, 15),
              'grey60': (153,153,153), 'grey61': (156,156,156),
              'grey62': (158,158,158), 'grey63': (161,161,161),
              'grey64': (163,163,163), 'grey65': (166,166,166),
              'grey66': (168,168,168), 'grey67': (171,171,171),
              'grey68': (173,173,173), 'grey69': (176,176,176),
              'grey7': ( 18, 18, 18), 'grey70': (179,179,179),
              'grey71': (181,181,181), 'grey72': (184,184,184),
              'grey73': (186,186,186), 'grey74': (189,189,189),
              'grey75': (191,191,191), 'grey76': (194,194,194),
              'grey77': (196,196,196), 'grey78': (199,199,199),
              'grey79': (201,201,201), 'grey8': ( 20, 20, 20),
              'grey80': (204,204,204), 'grey81': (207,207,207),
              'grey82': (209,209,209), 'grey83': (212,212,212),
              'grey84': (214,214,214), 'grey85': (217,217,217),
              'grey86': (219,219,219), 'grey87': (222,222,222),
              'grey88': (224,224,224), 'grey89': (227,227,227),
              'grey9': ( 23, 23, 23), 'grey90': (229,229,229),
              'grey91': (232,232,232), 'grey92': (235,235,235),
              'grey93': (237,237,237), 'grey94': (240,240,240),
              'grey95': (242,242,242), 'grey96': (245,245,245),
              'grey97': (247,247,247), 'grey98': (250,250,250),
              'grey99': (252,252,252), 'honeydew': (240,255,240),
              'honeydew1': (240,255,240), 'honeydew2': (224,238,224),
              'honeydew3': (193,205,193), 'honeydew4': (131,139,131),
              'hotpink': (255,105,180), 'hotpink1': (255,110,180),
              'hotpink2': (238,106,167), 'hotpink3': (205, 96,144),
              'hotpink4': (139, 58, 98), 'indianred': (205, 92, 92),
              'indianred1': (255,106,106), 'indianred2': (238, 99, 99),
              'indianred3': (205, 85, 85), 'indianred4': (139, 58, 58),
              'ivory': (255,255,240), 'ivory1': (255,255,240),
              'ivory2': (238,238,224), 'ivory3': (205,205,193),
              'ivory4': (139,139,131), 'khaki': (240,230,140),
              'khaki1': (255,246,143), 'khaki2': (238,230,133),
              'khaki3': (205,198,115), 'khaki4': (139,134, 78),
              'lavender': (230,230,250), 'lavenderblush': (255,240,245),
              'lavenderblush1': (255,240,245), 'lavenderblush2': (238,224,229),
              'lavenderblush3': (205,193,197), 'lavenderblush4': (139,131,134),
              'lawngreen': (124,252,  0), 'lemonchiffon': (255,250,205),
              'lemonchiffon1': (255,250,205), 'lemonchiffon2': (238,233,191),
              'lemonchiffon3': (205,201,165), 'lemonchiffon4': (139,137,112),
              'lightblue': (173,216,230), 'lightblue1': (191,239,255),
              'lightblue2': (178,223,238), 'lightblue3': (154,192,205),
              'lightblue4': (104,131,139), 'lightcoral': (240,128,128),
              'lightcyan': (224,255,255), 'lightcyan1': (224,255,255),
              'lightcyan2': (209,238,238), 'lightcyan3': (180,205,205),
              'lightcyan4': (122,139,139), 'lightgoldenrod': (238,221,130),
              'lightgoldenrod1': (255,236,139), 'lightgoldenrod2': (238,220,130),
              'lightgoldenrod3': (205,190,112), 'lightgoldenrod4': (139,129, 76),
              'lightgoldenrodyellow': (250,250,210), 'lightgreen': (144,238,144),
              'lightgrey': (211,211,211), 'lightpink': (255,182,193),
              'lightpink1': (255,174,185), 'lightpink2': (238,162,173),
              'lightpink3': (205,140,149), 'lightpink4': (139, 95,101),
              'lightsalmon': (255,160,122), 'lightsalmon1': (255,160,122),
              'lightsalmon2': (238,149,114), 'lightsalmon3': (205,129, 98),
              'lightsalmon4': (139, 87, 66), 'lightseagreen': ( 32,178,170),
              'lightskyblue': (135,206,250), 'lightskyblue1': (176,226,255),
              'lightskyblue2': (164,211,238), 'lightskyblue3': (141,182,205),
              'lightskyblue4': ( 96,123,139), 'lightslateblue': (132,112,255),
              'lightslategrey': (119,136,153), 'lightsteelblue': (176,196,222),
              'lightsteelblue1': (202,225,255), 'lightsteelblue2': (188,210,238),
              'lightsteelblue3': (162,181,205), 'lightsteelblue4': (110,123,139),
              'lightyellow': (255,255,224), 'lightyellow1': (255,255,224),
              'lightyellow2': (238,238,209), 'lightyellow3': (205,205,180),
              'lightyellow4': (139,139,122), 'limegreen': ( 50,205, 50),
              'linen': (250,240,230), 'magenta': (255,  0,255),
              'magenta1': (255,  0,255), 'magenta2': (238,  0,238),
              'magenta3': (205,  0,205), 'magenta4': (139,  0,139),
              'maroon': (176, 48, 96), 'maroon1': (255, 52,179),
              'maroon2': (238, 48,167), 'maroon3': (205, 41,144),
              'maroon4': (139, 28, 98), 'mediumaquamarine': (102,205,170),
              'mediumblue': (  0,  0,205), 'mediumorchid': (186, 85,211),
              'mediumorchid1': (224,102,255), 'mediumorchid2': (209, 95,238),
              'mediumorchid3': (180, 82,205), 'mediumorchid4': (122, 55,139),
              'mediumpurple': (147,112,219), 'mediumpurple1': (171,130,255),
              'mediumpurple2': (159,121,238), 'mediumpurple3': (137,104,205),
              'mediumpurple4': ( 93, 71,139), 'mediumseagreen': ( 60,179,113),
              'mediumslateblue': (123,104,238), 'mediumspringgreen': (  0,250,154),
              'mediumturquoise': ( 72,209,204), 'mediumvioletred': (199, 21,133),
              'midnightblue': ( 25, 25,112), 'mintcream': (245,255,250),
              'mistyrose': (255,228,225), 'mistyrose1': (255,228,225),
              'mistyrose2': (238,213,210), 'mistyrose3': (205,183,181),
              'mistyrose4': (139,125,123), 'moccasin': (255,228,181),
              'navajowhite': (255,222,173), 'navajowhite1': (255,222,173),
              'navajowhite2': (238,207,161), 'navajowhite3': (205,179,139),
              'navajowhite4': (139,121, 94), 'navy':  (  0,  0,128),
              'navyblue': (  0,  0,128), 'oldlace': (253,245,230),
              'olivedrab': (107,142, 35), 'olivedrab1': (192,255, 62),
              'olivedrab2': (179,238, 58), 'olivedrab3': (154,205, 50),
              'olivedrab4': (105,139, 34), 'orange': (255,165,  0),
              'orange1': (255,165,  0), 'orange2': (238,154,  0),
              'orange3': (205,133,  0), 'orange4': (139, 90,  0),
              'orangered': (255, 69,  0), 'orangered1': (255, 69,  0),
              'orangered2': (238, 64,  0), 'orangered3': (205, 55,  0),
              'orangered4': (139, 37,  0), 'orchid': (218,112,214),
              'orchid1': (255,131,250), 'orchid2': (238,122,233),
              'orchid3': (205,105,201), 'orchid4': (139, 71,137),
              'palegoldenrod': (238,232,170), 'palegreen': (152,251,152),
              'palegreen1': (154,255,154), 'palegreen2': (144,238,144),
              'palegreen3': (124,205,124), 'palegreen4': ( 84,139, 84),
              'paleturquoise': (175,238,238), 'paleturquoise1': (187,255,255),
              'paleturquoise2': (174,238,238), 'paleturquoise3': (150,205,205),
              'paleturquoise4': (102,139,139), 'palevioletred': (219,112,147),
              'palevioletred1': (255,130,171), 'palevioletred2': (238,121,159),
              'palevioletred3': (205,104,137), 'palevioletred4': (139, 71, 93),
              'papayawhip': (255,239,213), 'peachpuff': (255,218,185),
              'peachpuff1': (255,218,185), 'peachpuff2': (238,203,173),
              'peachpuff3': (205,175,149), 'peachpuff4': (139,119,101),
              'peru':  (205,133, 63), 'pink':  (255,192,203),
              'pink1': (255,181,197), 'pink2': (238,169,184),
              'pink3': (205,145,158), 'pink4': (139, 99,108),
              'plum':  (221,160,221), 'plum1': (255,187,255),
              'plum2': (238,174,238), 'plum3': (205,150,205),
              'plum4': (139,102,139), 'powderblue': (176,224,230),
              'purple': (160, 32,240), 'purple1': (155, 48,255),
              'purple2': (145, 44,238), 'purple3': (125, 38,205),
              'purple4': ( 85, 26,139), 'red':   (255,  0,  0),
              'red1':  (255,  0,  0), 'red2':  (238,  0,  0),
              'red3':  (205,  0,  0), 'red4':  (139,  0,  0),
              'rosybrown': (188,143,143), 'rosybrown1': (255,193,193),
              'rosybrown2': (238,180,180), 'rosybrown3': (205,155,155),
              'rosybrown4': (139,105,105), 'royalblue': ( 65,105,225),
              'royalblue1': ( 72,118,255), 'royalblue2': ( 67,110,238),
              'royalblue3': ( 58, 95,205), 'royalblue4': ( 39, 64,139),
              'saddlebrown': (139, 69, 19), 'salmon': (250,128,114),
              'salmon1': (255,140,105), 'salmon2': (238,130, 98),
              'salmon3': (205,112, 84), 'salmon4': (139, 76, 57),
              'sandybrown': (244,164, 96), 'seagreen': ( 46,139, 87),
              'seagreen1': ( 84,255,159), 'seagreen2': ( 78,238,148),
              'seagreen3': ( 67,205,128), 'seagreen4': ( 46,139, 87),
              'seashell': (255,245,238), 'seashell1': (255,245,238),
              'seashell2': (238,229,222), 'seashell3': (205,197,191),
              'seashell4': (139,134,130), 'sienna': (160, 82, 45),
              'sienna1': (255,130, 71), 'sienna2': (238,121, 66),
              'sienna3': (205,104, 57), 'sienna4': (139, 71, 38),
              'skyblue': (135,206,235), 'skyblue1': (135,206,255),
              'skyblue2': (126,192,238), 'skyblue3': (108,166,205),
              'skyblue4': ( 74,112,139), 'slateblue': (106, 90,205),
              'slateblue1': (131,111,255), 'slateblue2': (122,103,238),
              'slateblue3': (105, 89,205), 'slateblue4': ( 71, 60,139),
              'slategrey': (112,128,144), 'slategrey1': (198,226,255),
              'slategrey2': (185,211,238), 'slategrey3': (159,182,205),
              'slategrey4': (108,123,139), 'snow':  (255,250,250),
              'snow1': (255,250,250), 'snow2': (238,233,233),
              'snow3': (205,201,201), 'snow4': (139,137,137),
              'springgreen': (  0,255,127), 'springgreen1': (  0,255,127),
              'springgreen2': (  0,238,118), 'springgreen3': (  0,205,102),
              'springgreen4': (  0,139, 69), 'steelblue': ( 70,130,180),
              'steelblue1': ( 99,184,255), 'steelblue2': ( 92,172,238),
              'steelblue3': ( 79,148,205), 'steelblue4': ( 54,100,139),
              'tan':   (210,180,140), 'tan1':  (255,165, 79),
              'tan2':  (238,154, 73), 'tan3':  (205,133, 63),
              'tan4':  (139, 90, 43), 'thistle': (216,191,216),
              'thistle1': (255,225,255), 'thistle2': (238,210,238),
              'thistle3': (205,181,205), 'thistle4': (139,123,139),
              'tomato': (255, 99, 71), 'tomato1': (255, 99, 71),
              'tomato2': (238, 92, 66), 'tomato3': (205, 79, 57),
              'tomato4': (139, 54, 38), 'turquoise': ( 64,224,208),
              'turquoise1': (  0,245,255), 'turquoise2': (  0,229,238),
              'turquoise3': (  0,197,205), 'turquoise4': (  0,134,139),
              'violet': (238,130,238), 'violetred': (208, 32,144),
              'violetred1': (255, 62,150), 'violetred2': (238, 58,140),
              'violetred3': (205, 50,120), 'violetred4': (139, 34, 82),
              'wheat': (245,222,179), 'wheat1': (255,231,186),
              'wheat2': (238,216,174), 'wheat3': (205,186,150),
              'wheat4': (139,126,102), 'white': (255,255,255),
              'whitesmoke': (245,245,245), 'yellow': (255,255,  0),
              'yellow1': (255,255,  0), 'yellow2': (238,238,  0),
              'yellow3': (205,205,  0), 'yellow4': (139,139,  0),
              'yellowgreen': (154,205, 50)
              }

def rgb(color,default=(0,0,0)):
    """ return rgb tuple for named color in rgb.txt or a hex color """
    c = color.lower()
    if c[0:1] == '#' and len(c)==7:
        r,g,b = c[1:3], c[3:5], c[5:]
        r,g,b = [int(n, 16) for n in (r, g, b)]
        return (r,g,b)

    if c.find(' ')>-1:    c = c.replace(' ','')
    if c.find('gray')>-1: c = c.replace('gray','grey')
    if c in x11_colors.keys():  return x11_colors[c]
    return default

def hex2rgb(hex):
    c = hex
    if c[0:1] == '#' and len(c)==7:
        r,g,b = c[1:3], c[3:5], c[5:]
        r,g,b = [int(n, 16) for n in (r, g, b)]
        return (r,g,b)
    return rgb


def rgb2hex(rgb):
    if isinstance(rgb, tuple):
        col = '#%02x%02x%02x' % rgb[:3]
    else:
        try:
            col = '#%02x%02x%02x' % (rgb.Red(), rgb.Green(), rgb.Blue())
        except:
            col = "#000000"
    return col.upper()


def hexcolor(color):
    " returns hex color given a tuple, wx.Color, or X11 named color"
    # first, if this is a hex color already, return!
    if isinstance(color, (str, unicode)):
        if color[0] == '#' and len(color)==7:
            return color

    # now, get color to an rgb tuple
    rgb = (0,0,0)
    if isinstance(color, tuple):
        rgb = color
    elif isinstance(color, list):
        rgb = tuple(color)
    elif isinstance(color, (str, unicode)):
        c = color.lower()
        if c.find(' ')>-1:    c = c.replace(' ','')
        if c.find('gray')>-1: c = c.replace('gray','grey')
        if c in x11_colors:
            rgb = x11_colors[c]
    else:
        try:
            rgb = color.Red(), color.Green(), color.Blue()
        except:
            pass

    # convert rgb to hex color
    col = '#%02x%02x%02x' % (rgb)
    return col.upper()

###
###

## colormaps derived from IDL
custom_colormap_data = {
   "green_heat":(
(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,3,4,6,8,9,11,12,14,16,17,19,20,22,24,25,27,29,30,32,33,35,37,38,40,41,43,45,46,48,50,51,53,54,56,58,59,61,62,64,66,67,69,71,72,74,75,77,79,80,82,83,85,87,88,90,91,93,95,96,98,100,101,103,104,106,108,109,111,112,114,116,117,119,121,122,124,125,127,129,130,132,133,135,137,138,140,142,143,145,146,148,150,151,153,154,156,158,159,161,163,164,166,167,169,171,172,174,175,177,179,180,182,183,185,187,188,190,192,193,195,196,198,200,201,203,204,206,208,209,211,213,214,216,217,219,221,222,224,225,227,229,230,232,234,235,237,238,240,242,243,245,246,248,250,251,253,255),
(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255) ,
(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,6,10,13,17,20,24,27,31,34,37,41,44,48,51,55,58,62,65,68,72,75,79,82,86,89,93,96,99,103,106,110,113,117,120,124,127,130,134,137,141,144,148,151,155,158,161,165,168,172,175,179,182,186,189,192,196,199,203,206,210,213,217,220,223,227,230,234,237,241,244,248,251,255) ),
   "stdgamma":(
(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,9,14,19,23,28,33,38,42,47,52,57,61,66,71,76,81,81,81,81,81,81,81,81,80,80,80,80,80,80,80,79,84,89,94,99,104,109,114,119,124,129,134,139,144,149,154,159,164,169,174,180,185,190,196,201,206,212,217,222,228,233,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,248,240,232,225,217,209,202,194,186,179,171,163,168,173,178,183,188,193,198,203,209,214,219,224,229,234,239,244,249,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255) ,
(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,10,16,21,27,32,37,43,48,54,59,64,70,75,81,85,90,95,100,105,109,114,119,124,129,134,138,143,148,153,158,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,169,175,181,187,193,199,205,212,218,224,230,236,242,248,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255) ,
(0,5,10,15,20,26,31,36,41,46,52,57,62,67,72,78,83,88,93,98,104,109,114,119,124,130,135,140,145,150,156,161,166,171,176,182,187,192,197,202,208,213,218,223,228,234,239,244,249,255,250,245,239,234,228,223,218,212,207,201,196,190,185,180,174,169,163,158,152,147,142,136,131,125,120,114,109,104,98,93,87,82,76,71,66,60,55,49,44,38,33,28,22,17,11,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,9,14,19,24,28,33,38,43,48,53,57,62,67,72,77,82,77,71,65,59,53,47,41,36,30,24,18,12,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,6,9,12,16,19,22,25,29,32,35,38,41,45,48,51,54,58,61,64,67,71,74,77,80,83,87,90,93,96,100,103,106,109,112,116,119,122,125,129,132,135,138,142,145,148,151,154,158,161,164,167,171,174,177,180,183,187,190,193,196,200,203,206,209,213,216,219,222,225,229,232,235,238,242,245,248,251,255) ),
   "blue_heat":(
(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,9,13,17,21,25,29,33,37,41,45,49,53,57,61,65,69,73,77,81,85,90,94,98,102,106,110,114,118,122,126,130,134,138,142,146,150,154,158,162,166,170,175,179,183,187,191,195,199,203,207,211,215,219,223,227,231,235,239,243,247,251,255) ,
(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,4,5,7,9,10,12,13,15,17,18,20,21,23,25,26,28,29,31,33,34,36,37,39,41,42,44,45,47,49,50,52,53,55,57,58,60,61,63,65,66,68,69,71,73,74,76,77,79,81,82,84,85,87,89,90,92,94,95,97,98,100,102,103,105,106,108,110,111,113,114,116,118,119,121,122,124,126,127,129,130,132,134,135,137,138,140,142,143,145,146,148,150,151,153,154,156,158,159,161,162,164,166,167,169,170,172,174,175,177,179,180,182,183,185,187,188,190,191,193,195,196,198,199,201,203,204,206,207,209,211,212,214,215,217,219,220,222,223,225,227,228,230,231,233,235,236,238,239,241,243,244,246,247,249,251,252,254,255) ,
(0,1,2,4,5,6,8,9,10,12,13,14,16,17,18,20,21,23,24,25,27,28,29,31,32,33,35,36,37,39,40,42,43,44,46,47,48,50,51,52,54,55,56,58,59,61,62,63,65,66,67,69,70,71,73,74,75,77,78,80,81,82,84,85,86,88,89,90,92,93,94,96,97,99,100,101,103,104,105,107,108,109,111,112,113,115,116,118,119,120,122,123,124,126,127,128,130,131,132,134,135,136,138,139,141,142,143,145,146,147,149,150,151,153,154,155,157,158,160,161,162,164,165,166,168,169,170,172,173,174,176,177,179,180,181,183,184,185,187,188,189,191,192,193,195,196,198,199,200,202,203,204,206,207,208,210,211,212,214,215,217,218,219,221,222,223,225,226,227,229,230,231,233,234,236,237,238,240,241,242,244,245,246,248,249,250,252,253,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255) ),
   "red_heat":(
(0,1,2,4,5,7,8,10,11,13,14,15,17,18,20,21,23,24,26,27,28,30,31,33,34,36,37,39,40,42,43,44,46,47,49,50,52,53,55,56,57,59,60,62,63,65,66,68,69,70,72,73,75,76,78,79,81,82,84,85,86,88,89,91,92,94,95,97,98,99,101,102,104,105,107,108,110,111,113,114,115,117,118,120,121,123,124,126,127,128,130,131,133,134,136,137,139,140,141,143,144,146,147,149,150,152,153,155,156,157,159,160,162,163,165,166,168,169,170,172,173,175,176,178,179,181,182,184,185,186,188,189,191,192,194,195,197,198,199,201,202,204,205,207,208,210,211,212,214,215,217,218,220,221,223,224,226,227,228,230,231,233,234,236,237,239,240,241,243,244,246,247,249,250,252,253,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255) ,
(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,3,5,7,9,11,13,15,17,18,20,22,24,26,28,30,32,34,35,37,39,41,43,45,47,49,51,52,54,56,58,60,62,64,66,68,69,71,73,75,77,79,81,83,85,86,88,90,92,94,96,98,100,102,103,105,107,109,111,113,115,117,119,120,122,124,126,128,130,132,134,136,137,139,141,143,145,147,149,151,153,154,156,158,160,162,164,166,168,170,171,173,175,177,179,181,183,185,187,188,190,192,194,196,198,200,202,204,205,207,209,211,213,215,217,219,221,222,224,226,228,230,232,234,236,238,239,241,243,245,247,249,251,253,255) ,
(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,7,11,15,19,23,27,31,35,39,43,47,51,54,58,62,66,70,74,78,82,86,90,94,98,102,105,109,113,117,121,125,129,133,137,141,145,149,153,156,160,164,168,172,176,180,184,188,192,196,200,204,207,211,215,219,223,227,231,235,239,243,247,251,255) )
}

def register_custom_colormaps():
    """
    registers custom color maps
    """
    makemap = LinearSegmentedColormap.from_list
    for name, val in custom_colormap_data.items():
        cm1 = np.array(val).transpose().astype('f8')/256.0
        cm2 = cm1[::-1]
        nam1 = name
        nam2 = '%s_r' % name
        register_cmap(name=nam1, cmap=makemap(nam1, cm1, 256), lut=256)
        register_cmap(name=nam2, cmap=makemap(nam2, cm2, 256), lut=256)

    return ('stdgamma', 'red_heat', 'green_heat', 'blue_heat')
