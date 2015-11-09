#!/usr/bin/python
import sentence_generator



def main(): 
    test = sentence_generator.sentence_generator("txt/harrypotter.txt", 5)
    test.generate_sentence(100)

if __name__ == "__main__":
    main()
