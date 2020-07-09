import argparse
import glob
from lib.exam_loader import ExamLoader

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--exam_token", help="exam token")

args = vars(parser.parse_args())

if not args['exam_token']:
    print("An exam token is required to start an exam")
    print("Please provide an exam token like the following:")
    print("python start_exam.py -t [<EXAM_TOKEN>]")

if len(glob.glob('./tests/*')) != 0 or len(glob.glob('./answers/*')) != 0:
    print("Please make sure that the **answers** and **tests** directories are empty before trying to start an exam!")

else:
    ExamLoader().load(token = args['exam_token'])



