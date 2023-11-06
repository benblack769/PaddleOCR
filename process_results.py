import sys
import subprocess

pdf_fname = sys.argv[1]

subprocess.run(f'pdftoppm -png {pdf_fname}')

'python tools/infer/predict_system.py --image_dir=origins_of_intelligence_in_children.pdf --det_model_dir="./ch_PP-OCRv3_det_infer/" --rec_model_dir="./en_PP-OCRv3_rec_infer/" --use_angle_cls=false --rec_char_dict_path="ppocr/utils/en_dict.txt" --use_gpu=False'