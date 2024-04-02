from fontTools.colorLib.builder import buildCOLR, buildCPAL
from fontTools.ttLib import getTableModule, TTFont
from fontTools.ttLib.tables import otTables as ot

def color(hex: str):
  col = getTableModule('CPAL').Color.fromHex(hex)
  print(col)
  return col

font = TTFont("./sources/original/ttf/Weblight.ttf")

colors =[[(1.0, 0, 0, 1.0), (0, 1.0, 1.0, 1.0)]]
font["CPAL"] = buildCPAL(colors)

colrv1 = {}
layers = []
layers.append({
    "Format": ot.PaintFormat.PaintComposite,
      "CompositeMode": ot.CompositeMode.MULTIPLY,
      "SourcePaint": {
        "Format": ot.PaintFormat.PaintTranslate,
        "dx": -50,
        "dy": 0,
        "Paint": {
          "Format": ot.PaintFormat.PaintGlyph,
          "Paint": {
            "Format": ot.PaintFormat.PaintSolid,
            "PaletteIndex": 0,
            "Alpha": 1.0
          },
          "Glyph": "A"
        }
      },
      "BackdropPaint": {
        "Format": ot.PaintFormat.PaintTranslate,
        "dx": 50,
        "dy": 0,
        "Paint": {
          "Format": ot.PaintFormat.PaintGlyph,
          "Paint": {
            "Format": ot.PaintFormat.PaintSolid,
            "PaletteIndex": 1,
            "Alpha": 1.0
          },
          "Glyph": "A"
        }
      },
  })

colrv1["A"] = (ot.PaintFormat.PaintColrLayers, layers)

font["COLR"] = buildCOLR(colrv1, 1)

font.save('./build/WebLight02.ttf')