import json
import os 
from generators_paraphrasers import paraphrase_report, generate_image, convert_sent_to_paragraph


def main():

	prompt1 = "An X ray showing ankle fracture"
	prompt2 = "A chest x ray with rib fracture"
	prompt3 = "A chest x ray showing an AP view with minor hairline fracture in left clavicle"
	prompt4 = "A chest x ray with an LLIED device present" 
	prompt5 = "An X ray of the left knee" 
	prompt6 = "A PA view showing fracture on L3 vertebrae"
	prompt7 = "An X ray of the wrist with a small fracture on the thumb"
	prompt8 = "AN x ray of the elbow"
	prompt9 = "A hip x ray showing Avascular Necrosis"
	prompt10 = "A whole body x ray"

	prompt_list = [prompt1, prompt2, prompt3, prompt4, prompt5, prompt6, prompt7, prompt8, prompt9]
	prompt_list = [prompt10]

	step = 10
	for _prompt in prompt_list:
		fn = 'prompt' + str(step) + '.jpg'
		generate_image(_prompt, fn)
		step+=1



if __name__ == '__main__':
	main()
