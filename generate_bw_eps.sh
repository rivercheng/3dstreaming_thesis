#!/bin/bash
python plotWithColorMap.py
python color2bw.py heatmap_buddha.png heatmap_buddha_bw.png
python color2bw.py heatmap_dragon.png heatmap_dragon_bw.png
python color2bw.py heatmap_thai.png   heatmap_thai_bw.png
convert heatmap_buddha_bw.png heatmap_buddha_bw_temp.eps
convert heatmap_dragon_bw.png heatmap_dragon_bw_temp.eps
convert heatmap_thai_bw.png   heatmap_thai_bw_temp.eps
eps2eps heatmap_buddha_bw_temp.eps heatmap_buddha_bw.eps
eps2eps heatmap_dragon_bw_temp.eps heatmap_dragon_bw.eps
eps2eps heatmap_thai_bw_temp.eps heatmap_thai_bw.eps
rm -f heatmap_buddha_bw_temp.eps
rm -f heatmap_dragon_bw_temp.eps
rm -f heatmap_thai_bw_temp.eps


