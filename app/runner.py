import json
import os
from generators_paraphrasers import paraphrase_report, generate_image, convert_sent_to_paragraph
import shutil

def main():
    test_data = '/workspace/data/text'
    image_data = '/workspace/data/image'

    data_dir = './image_text_pair'
    p10_file = './image_text_pair/p10.json'
    fid = open(p10_file, 'r')
    image_text_pair_dict = json.load(fid)

    image_list = []
    caption_list = []

    output_dir = './out_dir'
    os.makedirs(output_dir, exist_ok=True)


    total = 50
    count = 0
    for k, v in image_text_pair_dict.items():

        report_dict = {}

        _image = v['IMAGE']
        _caption = v['FINDINGS']
        report_dict['original'] = _caption

        file_name = os.path.basename(_image).split('.')[0]
        subj_out_dir = os.path.join(output_dir, file_name)
        os.makedirs(subj_out_dir, exist_ok=True)

        generate_image(_caption, os.path.join(subj_out_dir, 'image_original_generated.jpg'))
        # Create Xray
        generate_image(_caption +' Show x ray', os.path.join(subj_out_dir, 'image_original_generated_x_ray.jpg'))

        paraphrase_rep = paraphrase_report(_caption, "pegasus")
        paragraph = convert_sent_to_paragraph(paraphrase_rep)
        report_dict['pegasus'] = paragraph
        generate_image(paragraph, os.path.join(subj_out_dir, 'image_pegasus.jpg'))
        generate_image(paragraph +' Show x ray', os.path.join(subj_out_dir, 'image_pegasus_generated_x_ray.jpg'))


        print("+"*10)
        paraphrase_rep = paraphrase_report(_caption, "T5")
        paragraph = convert_sent_to_paragraph(paraphrase_rep)
        report_dict['T5'] = paragraph
        generate_image(paragraph, os.path.join(subj_out_dir, 'image_T5.jpg'))
        generate_image(paragraph + ' Show x ray', os.path.join(subj_out_dir, 'image_T5_x_ray.jpg'))
        shutil.copy(_image, os.path.join(subj_out_dir, file_name + '.jpg'))
        report_dict['original_fn'] = _image

        out_rep_fn = os.path.join(subj_out_dir, 'reports.json')
        fid2 = open(out_rep_fn, 'w')
        json.dump(report_dict, fid2, indent=2)
        fid2.close()
        count += 1
        print("Progress ", str(count) + '/' + str(total))
        if count > total:
            break

if __name__ == '__main__':
    main()
