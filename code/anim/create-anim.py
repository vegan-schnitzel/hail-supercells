# state file generated using paraview version 5.11.0
# expanded to allow automation of hail visualizations
# run in poincare system python

import paraview
paraview.compatibility.major = 5
paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# adjust parameters here:
# choose simulation
MR = 21

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [906, 298]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.CenterOfRotation = [1.4210854715202004e-14, 1.4210854715202004e-14, 24.84375]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [0.0005052955680270622, -577.212386128504, 126.62170084158633]
renderView1.CameraFocalPoint = [1.4207427619132275e-14, 1.4341260446065248e-14, 24.84375]
renderView1.CameraViewUp = [9.878929559200295e-05, 0.17364790150877754, 0.9848077967513627]
renderView1.CameraViewAngle = 9.72972972972973
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 151.69818756589984
renderView1.UseColorPaletteForBackground = 0
renderView1.BackgroundColorMode = 'Gradient'
renderView1.BackEnd = ''

# init the 'GridAxes3DActor' selected for 'AxesGrid'
#renderView1.AxesGrid.UseCustomBounds = 1

# Properties modified on renderView1.AxesGrid
renderView1.AxesGrid.Visibility = 1
renderView1.AxesGrid.XTitle = ''
renderView1.AxesGrid.YTitle = ''
renderView1.AxesGrid.ZTitle = ''
renderView1.AxesGrid.ShowEdges = 0
renderView1.AxesGrid.CustomBounds = [-120.0, 120.0, -90.0, 90.0, 0.0, 50.0]
renderView1.AxesGrid.DataScale = [1.0, 1.0, 2.5]

renderView1.AxesGrid.XAxisUseCustomLabels = 1
renderView1.AxesGrid.XAxisLabels = [-100.0, -50.0, 0.0, 50.0, 100.0]

renderView1.AxesGrid.YAxisUseCustomLabels = 1
renderView1.AxesGrid.YAxisLabels = [-50.0, 0.0, 50.0]

renderView1.AxesGrid.ZAxisUseCustomLabels = 1
renderView1.AxesGrid.ZAxisLabels = [5.0, 10.0, 15.0]

renderView1.AxesGrid.XLabelFontSize = 48
renderView1.AxesGrid.YLabelFontSize = 48
renderView1.AxesGrid.ZLabelFontSize = 48

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
# layout/tab size in pixels
layout1.SetSize(906, 298)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'NetCDF Reader'
mR16_3D_qcnc = NetCDFReader(registrationName='MR16_3D_qc.nc',
                            FileName=[f'/home/rw0064fu/fortran/cm1/belegarbeit/anim/hail/MR{MR}/MR{MR}_3D_qc.nc'])
mR16_3D_qcnc.Dimensions = '(z, y, x)'
mR16_3D_qcnc.SphericalCoordinates = 0

# create a new 'Text'
heading = Text(registrationName='Heading')
heading.Text = f'MR{MR}'

# create a new 'NetCDF Reader'
mR16_2D_crefnc = NetCDFReader(registrationName='MR16_2D_cref.nc',
                              FileName=[f'/home/rw0064fu/fortran/cm1/belegarbeit/anim/hail/MR{MR}/MR{MR}_2D_cref.nc'])
mR16_2D_crefnc.Dimensions = '(y, x)'
mR16_2D_crefnc.SphericalCoordinates = 0

# create a new 'Temporal Interpolator'
temporalInterpolator2 = TemporalInterpolator(registrationName='TemporalInterpolator2', Input=mR16_2D_crefnc)

# create a new 'NetCDF Reader'
mR16_3D_qinc = NetCDFReader(registrationName='MR16_3D_qi.nc',
                            FileName=[f'/home/rw0064fu/fortran/cm1/belegarbeit/anim/hail/MR{MR}/MR{MR}_3D_qi.nc'])
mR16_3D_qinc.Dimensions = '(z, y, x)'
mR16_3D_qinc.SphericalCoordinates = 0

# create a new 'Annotate Time Filter'
annotateTimeFilter1 = AnnotateTimeFilter(registrationName='AnnotateTimeFilter1', Input=temporalInterpolator2)
annotateTimeFilter1.Format = 'time: {time:.1f} min'

# create a new 'NetCDF Reader'
mR16_3D_qgnc = NetCDFReader(registrationName='MR16_3D_qg.nc',
                            FileName=[f'/home/rw0064fu/fortran/cm1/belegarbeit/anim/hail/MR{MR}/MR{MR}_3D_qg.nc'])
mR16_3D_qgnc.Dimensions = '(z, y, x)'
mR16_3D_qgnc.SphericalCoordinates = 0

# create a new 'Append Attributes'
appendAttributes1 = AppendAttributes(registrationName='AppendAttributes1', Input=[mR16_3D_qgnc, mR16_3D_qcnc, mR16_3D_qinc])

# create a new 'Temporal Interpolator'
temporalInterpolator1 = TemporalInterpolator(registrationName='TemporalInterpolator1', Input=appendAttributes1)

# create a new 'Transform'
transform1 = Transform(registrationName='Transform1', Input=temporalInterpolator1)
transform1.Transform = 'Transform'

# init the 'Transform' selected for 'Transform'
transform1.Transform.Scale = [1.000000000000001, 1.0, 2.5000000000000018]

# create a new 'Calculator'
calculator2 = Calculator(registrationName='Calculator2', Input=transform1)
calculator2.ResultArrayName = 'qh_scaled'
calculator2.Function = 'qg*1000'

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=transform1)
calculator1.ResultArrayName = 'qc_scaled'
calculator1.Function = 'qc*1000'

# create a new 'Contour'
contour1qv = Contour(registrationName='Contour1-qv', Input=calculator1)
contour1qv.ContourBy = ['POINTS', 'qc_scaled']
contour1qv.Isosurfaces = [0.1]
contour1qv.PointMergeMethod = 'Uniform Binning'

# create a new 'Calculator'
calculator3 = Calculator(registrationName='Calculator3', Input=transform1)
calculator3.ResultArrayName = 'qi_scaled'
calculator3.Function = 'qi*1000'

# create a new 'Contour'
contour2hail = Contour(registrationName='Contour2-hail', Input=calculator2)
contour2hail.ContourBy = ['POINTS', 'qh_scaled']
contour2hail.Isosurfaces = [0.1, 5.0, 10.0]
contour2hail.PointMergeMethod = 'Uniform Binning'

# create a new 'Contour'
contour3qi = Contour(registrationName='Contour3-qi', Input=calculator3)
contour3qi.ContourBy = ['POINTS', 'qi_scaled']
contour3qi.Isosurfaces = [0.1]
contour3qi.PointMergeMethod = 'Uniform Binning'

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from contour1qv
contour1qvDisplay = Show(contour1qv, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
contour1qvDisplay.Representation = 'Surface'
contour1qvDisplay.ColorArrayName = [None, '']
contour1qvDisplay.Opacity = 0.2
contour1qvDisplay.SelectTCoordArray = 'None'
contour1qvDisplay.SelectNormalArray = 'None'
contour1qvDisplay.SelectTangentArray = 'None'
contour1qvDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
contour1qvDisplay.SelectOrientationVectors = 'None'
contour1qvDisplay.ScaleFactor = -2.0000000000000002e+298
contour1qvDisplay.SelectScaleArray = 'None'
contour1qvDisplay.GlyphType = 'Arrow'
contour1qvDisplay.GlyphTableIndexArray = 'None'
contour1qvDisplay.GaussianRadius = -1e+297
contour1qvDisplay.SetScaleArray = [None, '']
contour1qvDisplay.ScaleTransferFunction = 'PiecewiseFunction'
contour1qvDisplay.OpacityArray = [None, '']
contour1qvDisplay.OpacityTransferFunction = 'PiecewiseFunction'
contour1qvDisplay.DataAxesGrid = 'GridAxesRepresentation'
contour1qvDisplay.PolarAxes = 'PolarAxesRepresentation'
contour1qvDisplay.SelectInputVectors = [None, '']
contour1qvDisplay.WriteLog = ''

# show data from contour2hail
contour2hailDisplay = Show(contour2hail, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
contour2hailDisplay.Representation = 'Surface'
contour2hailDisplay.AmbientColor = [1.0, 0.3333333333333333, 0.0]
contour2hailDisplay.ColorArrayName = ['POINTS', '']
contour2hailDisplay.DiffuseColor = [1.0, 0.3333333333333333, 0.0]
contour2hailDisplay.Opacity = 0.3
contour2hailDisplay.SelectTCoordArray = 'None'
contour2hailDisplay.SelectNormalArray = 'Normals'
contour2hailDisplay.SelectTangentArray = 'None'
contour2hailDisplay.OSPRayScaleArray = 'qh_scaled'
contour2hailDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
contour2hailDisplay.SelectOrientationVectors = 'None'
contour2hailDisplay.ScaleFactor = 5.91733529399363
contour2hailDisplay.SelectScaleArray = 'qh_scaled'
contour2hailDisplay.GlyphType = 'Arrow'
contour2hailDisplay.GlyphTableIndexArray = 'qh_scaled'
contour2hailDisplay.GaussianRadius = 0.2958667646996815
contour2hailDisplay.SetScaleArray = ['POINTS', 'qh_scaled']
contour2hailDisplay.ScaleTransferFunction = 'PiecewiseFunction'
contour2hailDisplay.OpacityArray = ['POINTS', 'qh_scaled']
contour2hailDisplay.OpacityTransferFunction = 'PiecewiseFunction'
contour2hailDisplay.DataAxesGrid = 'GridAxesRepresentation'
contour2hailDisplay.PolarAxes = 'PolarAxesRepresentation'
contour2hailDisplay.SelectInputVectors = [None, '']
contour2hailDisplay.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour2hailDisplay.ScaleTransferFunction.Points = [7.237514495849609, 0.0, 0.5, 0.0, 7.238491058349609, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour2hailDisplay.OpacityTransferFunction.Points = [7.237514495849609, 0.0, 0.5, 0.0, 7.238491058349609, 1.0, 0.5, 0.0]

# show data from calculator3
calculator3Display = Show(calculator3, renderView1, 'StructuredGridRepresentation')

# trace defaults for the display properties.
calculator3Display.Representation = 'Outline'
calculator3Display.ColorArrayName = ['POINTS', '']
calculator3Display.SelectTCoordArray = 'None'
calculator3Display.SelectNormalArray = 'None'
calculator3Display.SelectTangentArray = 'None'
calculator3Display.OSPRayScaleArray = 'qi_scaled'
calculator3Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator3Display.SelectOrientationVectors = 'None'
calculator3Display.ScaleFactor = 23.950001525878935
calculator3Display.SelectScaleArray = 'qi_scaled'
calculator3Display.GlyphType = 'Arrow'
calculator3Display.GlyphTableIndexArray = 'qi_scaled'
calculator3Display.GaussianRadius = 1.1975000762939467
calculator3Display.SetScaleArray = ['POINTS', 'qi_scaled']
calculator3Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator3Display.OpacityArray = ['POINTS', 'qi_scaled']
calculator3Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator3Display.DataAxesGrid = 'GridAxesRepresentation'
calculator3Display.PolarAxes = 'PolarAxesRepresentation'
calculator3Display.ScalarOpacityUnitDistance = 1.2713105833537548
calculator3Display.SelectInputVectors = [None, '']
calculator3Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator3Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.7764296866953373, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator3Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.7764296866953373, 1.0, 0.5, 0.0]

# show data from contour3qi
contour3qiDisplay = Show(contour3qi, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
contour3qiDisplay.Representation = 'Surface'
contour3qiDisplay.ColorArrayName = ['POINTS', '']
contour3qiDisplay.Opacity = 0.2
contour3qiDisplay.SelectTCoordArray = 'None'
contour3qiDisplay.SelectNormalArray = 'Normals'
contour3qiDisplay.SelectTangentArray = 'None'
contour3qiDisplay.OSPRayScaleArray = 'qi_scaled'
contour3qiDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
contour3qiDisplay.SelectOrientationVectors = 'None'
contour3qiDisplay.ScaleFactor = 13.955655590952734
contour3qiDisplay.SelectScaleArray = 'qi_scaled'
contour3qiDisplay.GlyphType = 'Arrow'
contour3qiDisplay.GlyphTableIndexArray = 'qi_scaled'
contour3qiDisplay.GaussianRadius = 0.6977827795476367
contour3qiDisplay.SetScaleArray = ['POINTS', 'qi_scaled']
contour3qiDisplay.ScaleTransferFunction = 'PiecewiseFunction'
contour3qiDisplay.OpacityArray = ['POINTS', 'qi_scaled']
contour3qiDisplay.OpacityTransferFunction = 'PiecewiseFunction'
contour3qiDisplay.DataAxesGrid = 'GridAxesRepresentation'
contour3qiDisplay.PolarAxes = 'PolarAxesRepresentation'
contour3qiDisplay.SelectInputVectors = [None, '']
contour3qiDisplay.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour3qiDisplay.ScaleTransferFunction.Points = [0.10000000149011612, 0.0, 0.5, 0.0, 0.10001526027917862, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour3qiDisplay.OpacityTransferFunction.Points = [0.10000000149011612, 0.0, 0.5, 0.0, 0.10001526027917862, 1.0, 0.5, 0.0]

# show data from temporalInterpolator2
temporalInterpolator2Display = Show(temporalInterpolator2, renderView1, 'UniformGridRepresentation')

# get color transfer function/color map for 'cref'
crefLUT = GetColorTransferFunction('cref')
crefLUT.AutomaticRescaleRangeMode = 'Never'
crefLUT.EnableOpacityMapping = 1
crefLUT.TransferFunction2D = None
crefLUT.RGBPoints = [0.5, 0.0, 0.0, 0.5625, 8.025302413374305, 0.0, 0.0, 1.0, 25.401367670867916, 0.0, 1.0, 1.0, 34.062701085418695, 0.5, 1.0, 0.5, 42.72403449996949, 1.0, 1.0, 0.0, 60.04673543310546, 1.0, 0.0, 0.0, 68.70806884765625, 0.5, 0.0, 0.0]
crefLUT.ColorSpace = 'RGB'
crefLUT.NanColor = [1.0, 0.0, 0.0]
crefLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'cref'
crefPWF = GetOpacityTransferFunction('cref')
crefPWF.Points = [0.5, 0.0, 0.5, 0.0, 0.5099985341127111, 1.0, 0.5, 0.0, 68.70806884765625, 1.0, 0.5, 0.0]
crefPWF.ScalarRangeInitialized = 1

# get 2D transfer function for 'cref'
crefTF2D = GetTransferFunction2D('cref')

# trace defaults for the display properties.
temporalInterpolator2Display.Representation = 'Slice'
temporalInterpolator2Display.ColorArrayName = ['POINTS', 'cref']
temporalInterpolator2Display.LookupTable = crefLUT
temporalInterpolator2Display.SelectTCoordArray = 'None'
temporalInterpolator2Display.SelectNormalArray = 'None'
temporalInterpolator2Display.SelectTangentArray = 'None'
temporalInterpolator2Display.OSPRayScaleArray = 'cref'
temporalInterpolator2Display.OSPRayScaleFunction = 'PiecewiseFunction'
temporalInterpolator2Display.SelectOrientationVectors = 'None'
temporalInterpolator2Display.ScaleFactor = 23.95000152587891
temporalInterpolator2Display.SelectScaleArray = 'None'
temporalInterpolator2Display.GlyphType = 'Arrow'
temporalInterpolator2Display.GlyphTableIndexArray = 'None'
temporalInterpolator2Display.GaussianRadius = 1.1975000762939454
temporalInterpolator2Display.SetScaleArray = ['POINTS', 'cref']
temporalInterpolator2Display.ScaleTransferFunction = 'PiecewiseFunction'
temporalInterpolator2Display.OpacityArray = ['POINTS', 'cref']
temporalInterpolator2Display.OpacityTransferFunction = 'PiecewiseFunction'
temporalInterpolator2Display.DataAxesGrid = 'GridAxesRepresentation'
temporalInterpolator2Display.PolarAxes = 'PolarAxesRepresentation'
temporalInterpolator2Display.ScalarOpacityUnitDistance = 5.382244856649801
temporalInterpolator2Display.ScalarOpacityFunction = crefPWF
temporalInterpolator2Display.TransferFunction2D = crefTF2D
temporalInterpolator2Display.OpacityArrayName = ['POINTS', 'cref']
temporalInterpolator2Display.ColorArray2Name = ['POINTS', 'cref']
temporalInterpolator2Display.SliceFunction = 'Plane'
temporalInterpolator2Display.SelectInputVectors = [None, '']
temporalInterpolator2Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
temporalInterpolator2Display.ScaleTransferFunction.Points = [-35.22878646850586, 0.0, 0.5, 0.0, 69.27164459228516, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
temporalInterpolator2Display.OpacityTransferFunction.Points = [-35.22878646850586, 0.0, 0.5, 0.0, 69.27164459228516, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
temporalInterpolator2Display.SliceFunction.Origin = [1.4210854715202004e-14, 1.4210854715202004e-14, 0.0]

# show data from annotateTimeFilter1
annotateTimeFilter1Display = Show(annotateTimeFilter1, renderView1, 'TextSourceRepresentation')

# trace defaults for the display properties.
annotateTimeFilter1Display.WindowLocation = 'Upper Right Corner'
annotateTimeFilter1Display.FontFamily = 'Courier'
annotateTimeFilter1Display.FontSize = 20

# show data from heading
headingDisplay = Show(heading, renderView1, 'TextSourceRepresentation')

# trace defaults for the display properties.
headingDisplay.WindowLocation = 'Upper Left Corner'
headingDisplay.FontFamily = 'Courier'
headingDisplay.FontSize = 20

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# restore active source
SetActiveSource(heading)
# ----------------------------------------------------------------


#if __name__ == '__main__':
    # generate extracts
    #SaveExtracts(ExtractsOutputDirectory='extracts')

# get animation scene
animationScene1 = GetAnimationScene()

# Properties modified on animationScene1
animationScene1.PlayMode = 'Sequence'

# Properties modified on animationScene1
animationScene1.StartTime = 0.0

# Properties modified on animationScene1
animationScene1.EndTime = 180.0

# Properties modified on animationScene1
animationScene1.NumberOfFrames = 91

# save animation
SaveAnimation(f'/home/rw0064fu/fortran/cm1/belegarbeit/anim/hail/MR{MR}/frames/fig.png',
              renderView1,
              ImageResolution=[3624, 1192],
              FrameWindow=[0, 90])
