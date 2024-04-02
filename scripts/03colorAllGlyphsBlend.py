from fontTools.colorLib.builder import buildCOLR, buildCPAL
from fontTools.ttLib import getTableModule, TTFont
from fontTools.ttLib.tables import otTables as ot
import random

def color(hex: str):
  col = getTableModule('CPAL').Color.fromHex(hex)
  print(col)
  return col

font = TTFont("./sources/original/ttf/Weblight.ttf")
glyphs = font.getGlyphSet()

colors =[[(1.0, 0, 0, 1.0), (0, 1.0, 1.0, 1.0)]]
font["CPAL"] = buildCPAL(colors)

colrv1 = {}

for glyph in glyphs:
  random_distance = random.randrange(-100, 100)
  layers = []
  layers.append({
      "Format": ot.PaintFormat.PaintComposite,
        "CompositeMode": ot.CompositeMode.MULTIPLY,
        "SourcePaint": {
          "Format": ot.PaintFormat.PaintTranslate,
          "dx": random_distance,
          "dy": 0,
          "Paint": {
            "Format": ot.PaintFormat.PaintGlyph,
            "Paint": {
              "Format": ot.PaintFormat.PaintSolid,
              "PaletteIndex": 0,
              "Alpha": 1.0
            },
            "Glyph": glyph
          }
        },
        "BackdropPaint": {
          "Format": ot.PaintFormat.PaintTranslate,
          "dx": -random_distance,
          "dy": 0,
          "Paint": {
            "Format": ot.PaintFormat.PaintGlyph,
            "Paint": {
              "Format": ot.PaintFormat.PaintSolid,
              "PaletteIndex": 1,
              "Alpha": 1.0
            },
            "Glyph": glyph
          }
        },
    })

  colrv1[glyph] = (ot.PaintFormat.PaintColrLayers, layers)

font["COLR"] = buildCOLR(colrv1, 1)

font.save('./build/WebLight03.ttf')