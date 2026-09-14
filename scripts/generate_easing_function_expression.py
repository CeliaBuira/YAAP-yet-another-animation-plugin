import os
from qgis.PyQt.QtCore import QEasingCurve
import numpy as np
import cairosvg
#from PIL import Image

def capitalized2snakecase(string):
    return "".join([("_"+i if i.isupper() else i) for i in string]).strip("_").lower()

"""
for i in QEasingCurve.Type:
    keep = False
    name = i.name
    if name.startswith("In"):
        keep = True
    if name.startswith("Out"):
        keep = True
    if name.startswith("InOut"):
        keep = True
    if name.startswith("OutIn"):
        keep = True
        
    if name == "InCurve" or name == "OutCurve":
        #legacy of Qt we don't care
        keep = False
    
    if keep:
        print(f'QEasingCurve.Type.{name}: "{name}",')        
"""

#itself Generate with code above 
mapping = {
    QEasingCurve.Type.InQuad: "InQuad",
    QEasingCurve.Type.OutQuad: "OutQuad",
    QEasingCurve.Type.InOutQuad: "InOutQuad",
    QEasingCurve.Type.OutInQuad: "OutInQuad",
    QEasingCurve.Type.InCubic: "InCubic",
    QEasingCurve.Type.OutCubic: "OutCubic",
    QEasingCurve.Type.InOutCubic: "InOutCubic",
    QEasingCurve.Type.OutInCubic: "OutInCubic",
    QEasingCurve.Type.InQuart: "InQuart",
    QEasingCurve.Type.OutQuart: "OutQuart",
    QEasingCurve.Type.InOutQuart: "InOutQuart",
    QEasingCurve.Type.OutInQuart: "OutInQuart",
    QEasingCurve.Type.InQuint: "InQuint",
    QEasingCurve.Type.OutQuint: "OutQuint",
    QEasingCurve.Type.InOutQuint: "InOutQuint",
    QEasingCurve.Type.OutInQuint: "OutInQuint",
    QEasingCurve.Type.InSine: "InSine",
    QEasingCurve.Type.OutSine: "OutSine",
    QEasingCurve.Type.InOutSine: "InOutSine",
    QEasingCurve.Type.OutInSine: "OutInSine",
    QEasingCurve.Type.InExpo: "InExpo",
    QEasingCurve.Type.OutExpo: "OutExpo",
    QEasingCurve.Type.InOutExpo: "InOutExpo",
    QEasingCurve.Type.OutInExpo: "OutInExpo",
    QEasingCurve.Type.InCirc: "InCirc",
    QEasingCurve.Type.OutCirc: "OutCirc",
    QEasingCurve.Type.InOutCirc: "InOutCirc",
    QEasingCurve.Type.OutInCirc: "OutInCirc",
    QEasingCurve.Type.InElastic: "InElastic",
    QEasingCurve.Type.OutElastic: "OutElastic",
    QEasingCurve.Type.InOutElastic: "InOutElastic",
    QEasingCurve.Type.OutInElastic: "OutInElastic",
    QEasingCurve.Type.InBack: "InBack",
    QEasingCurve.Type.OutBack: "OutBack",
    QEasingCurve.Type.InOutBack: "InOutBack",
    QEasingCurve.Type.OutInBack: "OutInBack",
    QEasingCurve.Type.InBounce: "InBounce",
    QEasingCurve.Type.OutBounce: "OutBounce",
    QEasingCurve.Type.InOutBounce: "InOutBounce",
    QEasingCurve.Type.OutInBounce: "OutInBounce",
}

# Easing curve as approximated cubic bezier
# Calculated using Least squares regression
# from https://github.com/zz85/cubic-bezier-approximations/blob/d1d42b672d11e03e60a9d1a6ca3c0b1d5748d6d8/easing.js#L70
interpolations_map = {
# Easing Curve type : bezier curve approximation (see above)
  QEasingCurve.Type.Linear : [0,0,1,1],
  QEasingCurve.Type.InQuad : [ 0.26, 0, 0.6, 0.2 ],
  QEasingCurve.Type.OutQuad : [ 0.4, 0.8, 0.74, 1 ] ,
  QEasingCurve.Type.InOutQuad : [ 0.48, 0.04, 0.52, 0.96 ] ,
  QEasingCurve.Type.OutInQuad : None,
  QEasingCurve.Type.InCubic : [ 0.4, 0, 0.68, 0.06 ],
  QEasingCurve.Type.OutCubic : [ 0.32, 0.94, 0.6, 1 ],
  QEasingCurve.Type.InOutCubic : [ 0.66, 0, 0.34, 1 ],
  QEasingCurve.Type.OutInCubic : None ,
  QEasingCurve.Type.InQuart : [ 0.52, 0, 0.74, 0 ],
  QEasingCurve.Type.OutQuart :  [ 0.26, 1, 0.48, 1 ],
  QEasingCurve.Type.InOutQuart :  [ 0.76, 0, 0.24, 1 ],
  QEasingCurve.Type.OutInQuart : None,
  QEasingCurve.Type.InQuint : [ 0.64, 0, 0.78, 0 ],
  QEasingCurve.Type.OutQuint : [ 0.22, 1, 0.36, 1 ],
  QEasingCurve.Type.InOutQuint : None,
  QEasingCurve.Type.OutInQuint :  None ,
  QEasingCurve.Type.InSine : [ 0.32, 0, 0.6, 0.36 ],
  QEasingCurve.Type.OutSine : [ 0.4, 0.64, 0.68, 1 ],
  QEasingCurve.Type.InOutSine : [ 0.36, 0, 0.64, 1 ],
  QEasingCurve.Type.OutInSine : None,
  QEasingCurve.Type.InExpo : [ 0.66, 0, 0.86, 0 ] ,
  QEasingCurve.Type.OutExpo :  [ 0.14, 1, 0.34, 1 ],
  QEasingCurve.Type.InOutExpo : [ 0.84, -0.12, 0.16, 1.0 ],
  QEasingCurve.Type.OutInExpo : None,
  QEasingCurve.Type.InCirc : [ 0.54, 0, 1, 0.44 ],
  QEasingCurve.Type.OutCirc : [ 0, 0.56, 0.46, 1 ],
  QEasingCurve.Type.InOutCirc : [ 0.88, 0.14, 0.12, 0.86 ],
  QEasingCurve.Type.OutInCirc : None
} 

def svg_for_curve(easing_curve_type):
    width = 32
    height = 32
    stroke_width = 4
    steps = 50
    svg_template = """
<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
  <path
    d="{path}"
    style="fill:none;stroke-width:{stroke_width};stroke-linecap:round;stroke-linejoin:round;stroke:#212121" 
    transform="translate(2, 2)"
    />
</svg>
"""

    # Shape of the curve
    curve = QEasingCurve(easing_curve_type)
    control_points =  interpolations_map.get(easing_curve_type, None)
    
    # if( curve.type() == QEasingCurve.Type.InSine ): print(control_points)
    path_ctrl_pts = ""
    if control_points is not None:
        #use bezier approximation for better scaling and reduce outputted file size 
      c_x1, c_y1, c_x2, c_y2 = control_points
    #   if( curve.type() == QEasingCurve.Type.InSine ): print(c_x1, c_y1, c_x2, c_y2)
      path_ctrl_pts = "M 0 {height} C {c_x1} {c_y1}, {c_x2} {c_y2}, {width} 0"
      path_ctrl_pts = path_ctrl_pts.format(height=height,
                          width=width,
                          c_x1=round(c_x1 * width, 3),
                          c_y1=round(height - (c_y1 * height) ,3),
                          c_x2=round(c_x2 * width, 3),
                          c_y2=round(height - (c_y2 * height), 3))
      path = path_ctrl_pts
    else:
      if( curve.type() == QEasingCurve.Type.InSine ): print("should not fallback ?")
      x = np.linspace(0, width, steps)
      y = [ height - ((height) * curve.valueForProgress(i/width)) for i in x]
      points = [(x, y) for x, y in zip(x, y)]
      path_segmentize = f"M {points[0][0]} {points[0][1]}"
      for i, j in points[1:]:
          path_segmentize += f" L {i} {j}"
      path = path_segmentize

    svg = svg_template.format(width=width+stroke_width,
                                    height=height+stroke_width,
                                    path=path,
                                #  stops=stops,
                                    stroke_width=stroke_width)

    return svg

# mapping = {k: capitalized2snakecase(v) for k, v in mapping.items()}


template = """@qgsfunction(group="Animation", referenced_columns=[])
def {name}(t, parent):
    \"""
    <h4>Syntax</h4>
    <p><b>{name}</b>(  <i> t </i>)</p>

    <h4>Arguments</h4>
    <p><i>t</i>: a float representing the progress of the animation (0 to 1)</p>


    
    <h4>Example usage</h4>
    <ul>
      <li><b>{name}</b>( 0.25 )  &rarr; {res_25}</li>
      <li><b>{name}</b>( 0.5 )  &rarr; {res_50}</li>
      <li><b>{name}</b>( 0.75 )  &rarr; {res_75}</li>
    </ul>
    \"""
    easing = QEasingCurve({qt_name})
    return easing.valueForProgress(t)"""

"""
for k, v in mapping.items():
    name = capitalized2snakecase(v)
    qt_name = k.name
    doc = template_doc.format(name=name)
    print(template.format(name=name, qt_name=qt_name, doc=doc))
    print("")
"""

target_file = r"C:\Users\Valentin\Documents\plugin-animation-interpolation-expressions\animation_interpolation_expressions\easing_autogenerated.py"

with open(target_file, "w+") as f:
    
    f.write( "# /!\\/!\\warning/!\\/!\\\n" )
    filename = os.path.basename(__file__)
    f.write( f"# autogenerated by {filename}\n\n" )
    f.write( "from qgis.PyQt.QtCore import QEasingCurve\n" )
    f.write("from qgis.utils import qgsfunction\n\n")
    
    f.write("registered_easing_functions = {\n")
    for k, v in mapping.items():
        
        f.write(f"    '{capitalized2snakecase(v)}'\n")
    f.write("}\n\n")

    for k, v in mapping.items():
        name  = capitalized2snakecase(v)
        qt_name = f"QEasingCurve.Type.{v}"
        svg = svg_for_curve(k)
        # curve_png_path = os.path.join(os.path.dirname(__file__), f"{v}_curve.png")
        # curve_svg_path = os.path.join(os.path.dirname(__file__), f"{v}_curve.svg")
        # with open(curve_svg_path, "w", encoding="utf-8") as svg_file:
        #     svg_file.write(svg)
        # print(curve_png_path)
        # cairosvg.svg2png(
        #     bytestring=svg.encode("utf-8"),
        #     write_to=curve_png_path,
        #     output_width=128,
        #     output_height=128,
        # )
        
        """
        img = Image.open(curve_png_path)
        img = img.resize((128, 128), Image.Resampling.LANCZOS)
        img.save(curve_png_path)
        """

        easing = QEasingCurve(k)
        
        def round_result(t):
            if round(t, 5) == t:
                return t
            return str(round(easing.valueForProgress(0.75), 5))+"…"
            
        
        func_expression_formated = template.format(name=name,
                               qt_name=qt_name,
                            #    img_src=curve_png_path,
                               res_25=round_result(easing.valueForProgress(0.25)),
                               res_50=round_result(easing.valueForProgress(0.5)),
                               res_75=round_result(easing.valueForProgress(0.75)),
                               svg=svg)
        f.write(func_expression_formated + "\n\n")
        