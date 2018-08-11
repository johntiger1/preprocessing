
import gensim
import spacy
import os
import nltk

from tqdm import tqdm
# myfile1.txt was the full text, while the cat file was just a small ish file created from the top n rows
nlp = spacy.load('en_core_web_lg')

# nltk.download("punkt")
with open("baseline_catfile.txt", "r") as file, open("processed_catfile.txt", "a") as write_file:

# actually, I just want to remove all dates. I can keep the rest (==Service etc.)
#     for lineNo, line in enumerate(file):
#         first_bit = line[0:100]
#         if "Service" not in first_bit and "Admission" not in first_bit:
#             print("breakage")
#             print(line[100:], lineNo)
#             break


    for lineNo, line in (enumerate(tqdm(file))):

        # if (lineNo == 0):
        # line = line.replace("\\n", "\n")
        # print(gensim.utils.simple_preprocess(line))
        # print("nltk")
        # print(nltk.sent_tokenize(line))
        # print("spacy")
        doc = nlp(line)

        for sent in doc.sents:
            # empirically this would be good
            # we definitley want the punctuation

            if len(str(sent).split()) > 3:

                write_file.write(str(sent))
                write_file.write("\n")
                # print("this is a " + str(sent))


        # sentences = [sent.string.strip() for sent in doc.sents]
        #
        # for sent in sentences:
        #
        #    print(sentences)



    #     print("HYBRID")
    #     # for sent in sentences:
    #     #     # rationale: it's more the text and not the numbers that matter
    #     #     # the first one (Spacy) splits the text into sentences. The next one (gensim) does some more preprocessing (like number removal)
    #     #
    #     #     # however, we probably DO want the punctuation to be apparent
    #     #     # print(gensim.utils.simple_preprocess(sent))
    #     #
    #     #
    #     #     procced = gensim.utils.simple_preprocess(sent)
    #     #     if len(procced) > 0 and 'namepattern' not in procced:
    #     #         print(procced)
    #
    #             # write_file.write(procced + )
    #
    #     # if small sentences, then we should: amalgamate things
    #     input()
    #
    #
    #     # break
    #     # first_bit = line[0:100]
    #     k = line.rfind("Date")
    #     print(k)
    #
    #
    #     if k < 100:
    #         print (line[0:k])
    #     # if k > 100 and k < 300:
    #     #     print (line)
    #     #     break
    #
    #
    #     if "Date" not in line:
    #         k = line.rfind("Date")
    #         print("breakage")
    #         print(line, lineNo)
    #         break
    #
    #
    # if (lineNo % 10000) ==0:
    #     print("done processing {}".format(lineNo))
    #     # split on "Chief complaint"
