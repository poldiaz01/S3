import os

# Comanda per a obtenir el video redimensionat a 480p
os.system("ffmpeg -i bbbVideo.mp4 -vf scale=-1:480 ex1_480p.mp4")

# Comanda per a convertir el video redimensionat a VP8
os.system("ffmpeg -i ex1_480p.mp4 -c:v libvpx -crf 30 -b:v 0 -b:a 128k -c:a libopus ex1_vp8.webm")

# Comanda per a convertir el video redimensionat a VP9
os.system("ffmpeg -i ex1_480p.mp4 -c:v libvpx-vp9 -crf 30 -b:v 0 -b:a 128k -c:a libopus ex1_vp9.webm")

# Comanda per a convertir el video redimensionat a h265
os.system("ffmpeg -i ex1_480p.mp4 -c:v libx265 -c:a copy ex_1_h265.mp4")

# Comanda per a convertir el video redimensionat a AV1
os.system("ffmpeg -i ex1_480p.mp4 -c:v libaom-av1 -crf 30 ex_1.av1.mkv")

# Comanda per a generar el mosaic dels 4 outputs previs
os.system('ffmpeg ' \
	'-i ex1_vp8.webm -i ex1_vp9.webm -i ex_1_h265.mp4 -i ex_1.av1.mkv ' \
	'-filter_complex "' \
		'nullsrc=size=640x480 [base];' \
		'[0:v] setpts=PTS-STARTPTS, scale=320x240 [upperleft];' \
		'[1:v] setpts=PTS-STARTPTS, scale=320x240 [upperright];' \
		'[2:v] setpts=PTS-STARTPTS, scale=320x240 [lowerleft];' \
		'[3:v] setpts=PTS-STARTPTS, scale=320x240 [lowerright];' \
		'[base][upperleft] overlay=shortest=1 [tmp1];' \
		'[tmp1][upperright] overlay=shortest=1:x=320 [tmp2];' \
		'[tmp2][lowerleft] overlay=shortest=1:y=240 [tmp3];' \
		'[tmp3][lowerright] overlay=shortest=1:x=320:y=240' \
	'" ' \
	'-c:v libx264 mosaic.mkv')




