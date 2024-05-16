#xport LIBGL_ALWAYS_SOFTWARE=1
#export MESA_GL_VERSION_OVERRIDE=3.3
export LIBGL_DRI3_DISABLE=1
gz sim -v4 -r iris_runway.sdf
#gz sim -v4 -r iris_warehouse.sdf
#gz sim -v4 -r gimbal.sdf