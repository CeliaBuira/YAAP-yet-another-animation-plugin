#-----------------------------------------------------------
# Copyright (C) 2015 Martin Dobias
#-----------------------------------------------------------
# Licensed under the terms of GNU GPL 2
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#---------------------------------------------------------------------

from qgis.PyQt.QtWidgets import QAction, QMessageBox
from qgis.PyQt.QtCore import QEasingCurve
from qgis.core import QgsExpression, qgsfunction

# from .easing import ease_in_circ as _ease_in_circ
from . import easing

def classFactory(iface):
    return MinimalPlugin(iface)


@qgsfunction(group="Animation", referenced_columns=[], handlesnull=True)
def lerp(start, end, t, unclamped=False):
    """
    <p> Equivalent of <i>scale_linear(t, 0, 1, start, end)</i> </p>
    <h4>Syntax</h4>
    <p><b>lerp</b>(  <i>start, end, value </i>)</p>

    <h4>Arguments</h4>
    <p><i>start</i> &rarr; placeholder</p>
    <p><i>end</i> &rarr; placeholder</p>
    <p><i>value</i> &rarr; placeholder</p>

    """
    if unclamped is None or unclamped != True:
        t = easing.clamp01(t)
        
    return (1-t) * start + t * end 


@qgsfunction(group="Animation", referenced_columns=[])
def lerp_unclamped(start, end, t, parent):
    """
    <p> Equivalent of <i>scale_linear(t, 0, 1, start, end)</i> </p>
    <h4>Syntax</h4>
    <p><b>lerp</b>(  <i>start, end, value </i>)</p>

    <h4>Arguments</h4>
    <p><i>start</i> &rarr; placeholder</p>
    <p><i>end</i> &rarr; placeholder</p>
    <p><i>value</i> &rarr; placeholder</p>
    """
    return (1-t) * start + t * end 


@qgsfunction(group="Animation", referenced_columns=[])
def inverse_lerp(start, end, value, parent):
    """
    <h4>Syntax</h4>
    <p><b>inverse_lerp</b>(  <i>start, stop, value </i>)</p>

    <h4>Arguments</h4>
    <p><i>start</i> &rarr; placeholder</p>
    <p><i>end</i> &rarr; placeholder</p>
    <p><i>value</i> &rarr; placeholder</p>
    """
    return easing.inverse_lerp(start, end, value)


@qgsfunction(group="Animation", referenced_columns=[])
def inverse_lerp_unclamped(start, end, value, parent):
    """
    <h4>Syntax</h4>
    <p><b>inverse_lerp</b>(  <i>start, stop, value </i>)</p>

    <h4>Arguments</h4>
    <p><i>start</i> &rarr; placeholder</p>
    <p><i>end</i> &rarr; placeholder</p>
    <p><i>value</i> &rarr; placeholder</p>
    """
    return easing.inverse_lerp_unclamped(start, end, value)

@qgsfunction(group="Animation", referenced_columns=[])
def ease_in_circ(start, end, t, parent):
    return easing.ease_in_circ(start, end, t)


def _ease_out_quad(t):
    easing = QEasingCurve(QEasingCurve.OutQuad)
    return easing.valueForProgress(t)

@qgsfunction(group="Animation", referenced_columns=[])
def ease_out_quad(t, parent):
    """
    <h4>Syntax</h4>
    <p><b>ease_out_quad</b>(  <i> t </i>)</p>
    """
    return _ease_out_quad(t)



@qgsfunction(group="Animation", referenced_columns=[])
def ease_in_sin(t, parent):
    """
    <h4>Syntax</h4>
    <p><b>ease_out_sin</b>(  <i> t </i>)</p>
    """
    easing = QEasingCurve(QEasingCurve.InSine)
    return easing.valueForProgress(t)


@qgsfunction(group="Animation", referenced_columns=[])
def ease_out_sin(t, parent):
    """
    <h4>Syntax</h4>
    <p><b>ease_out_sin</b>(  <i> t </i>)</p>
    """
    easing = QEasingCurve(QEasingCurve.OutSine)
    return easing.valueForProgress(t)


@qgsfunction(group="Animation", referenced_columns=[])
def ease_in_out_sin(t, parent):
    """
    <h4>Syntax</h4>
    <p><b>ease_out_sin</b>(  <i> t </i>)</p>
    """
    easing = QEasingCurve(QEasingCurve.InOutSine)
    return easing.valueForProgress(t)

@qgsfunction(group="Animation", referenced_columns=[])
def remap(value, start1, stop1, start2, stop2):
    """
    <h4>Syntax</h4>
    <p><b>remap</b>( value, start1, stop1, start2, stop2 )</p>
    """
    t = easing.inverse_lerp(start1, stop1, value)
    #return t
    return start2 + (stop2 - start2) * t

class MinimalPlugin:
    def __init__(self, iface):
        self.iface = iface

    def initGui(self):
        self.action = QAction('Go!', self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addToolBarIcon(self.action)

    def unload(self):
        self.iface.removeToolBarIcon(self.action)
        del self.action

        self.unloadExpressions()

    def run(self):
        QMessageBox.information(None, 'Minimal plugin', 'Do something useful here')

    def initExpressions(self):
        QgsExpression.registerFunction(inverse_lerp)

    def unloadExpressions(self):
        QgsExpression.unregisterFunction("inverse_lerp")

