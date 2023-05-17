import cairosvg

svg_code = '''
[{"content":"CoordiSpot","fontFamily":"Riffic Bold","fontSize":66,"fontStyle":"normal","fontVariant":"normal","fontWeight":400,"letterSpacing":0,"lineHeight":"normal","paintOrder":"stroke fill","searchTerm":"","textAlign":"center","textDecoration":"none","textTransform":"none","wordSpacing":0,"fitText":true,"whiteSpace":"pre-wrap","bbox":{"x":587,"y":363,"width":656.8096813092161,"height":79.13017498932992},"blend":"normal","childrenOpen":true,"id":"e214343b-1ed2-4c00-bb10-bfa40358ef96","idx":1,"opacity":1,"seed":1149178960,"type":"fancyText","visible":true,"exportable":true,"findable":true,"lock":false,"lockTransform":false,"selectable":true,"fill":{"type":"color","color":"#60b0f4","enabled":true}},{"searchTerm":"mouse","src":"#asset-1302656","svgPatch":{"defs":{},"patches":{"1":{"fill":"#60b0f4","fillOpacity":1},"2":{"fill":"#60b0f4","fillOpacity":1}}},"bbox":{"x":1110,"y":355,"width":200,"height":303.2258064516129,"scale":{"x":0.31561461794019935,"y":0.31561461794019935}},"blend":"normal","childrenOpen":true,"id":"71c15063-a0d4-4171-9032-9d0060e38543","idx":2,"opacity":1,"seed":548010694,"type":"clipart","visible":true,"exportable":true,"findable":true,"lock":false,"lockTransform":false,"selectable":true}]
'''

output_file = 'logo.png'

cairosvg.svg2png(bytestring=svg_code, write_to=output_file)
