# Free-Field-displacement-get
用于读取自由场土体位移坐标

1. 首先读取各个Tracer的坐标到COOR_BFAF.csv
2. 导出各个Tracer的位移
3. 把1， 2拼到一起，然后再map
4. 利用output_u3.py导出y_matrix
5. 利用1d_interval.py差值调整interval
