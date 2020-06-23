cdef extern from "header.h":
		double M_PI
        float MAX(float a, float b)
        double hypot(double x, double y)

		ctypedef int integral
		ctypedef double real

        void func(integral a, integral b, real c)
        real *func_arrays(integral[] i, integral[][10] j, real **k)
