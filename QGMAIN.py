import aqgFunction


# Main Function
def HELLO():
    # Create AQG object
    aqg = aqgFunction.AutomaticQuestionGenerator()

    # inputTextPath = "input file path -- ?? ../DB/db.txt"
    # readFile = open(inputTextPath, 'r+', encoding="utf8")
    #readFile = open(inputTextPath, 'r+', encoding="utf8", errors = 'ignore')

    # inputText = readFile.read()
    # inputText = 'Whilst technologies, such as psychophysiological measurements in general and electroencephalograms (EEG) in particular, have been around and continually improving for many years, future technologies promise to revolutionise the emerging Information Society through the development of brain-computer interfaces and augmented cognition solutions. This paper explores critical psychological and pragmatic issues that must be understood before these technologies can deliver their potential well. Within the context of HCI, we examined a sample (n = 105) BCI papers and found that the majority of research aimed to provide communication and control resources to people with disabilities or with extreme task demands. However, the concepts of usability and accessibility, and respective findings from their substantial research literatures were rarely applied explicitly but referenced implicitly. While this suggests an increased awareness of these concepts and the related large research literatures, the task remains to sharpen these concepts and to articulate their obvious relevance to BCI work.'
    # inputText = '''My best friend and I have been studying in the same school since kindergarten. We have been classmates each year at school. We share a very close bond and have a special friendship that we cherish and treasure. My friend is my partner, sitting beside me in class. She is kindly and helpful, and if I have any difficulties in understanding any topic in my studies, or in completing my homework or school project, she helps me. She is brilliant in mathematics and the sciences, while I am good at English. So we both help each other in whatever way possible. She helps me without ever belittling me. I greatly appreciate the quality in her. She does not make me feel obliged. There is a slight chance of rain today.'''
    inputText = '''Shah Jahan was widely considered to be the most competent of Emperor Jahangir's four sons and after Jahangir's death in late 1627, when a war of succession ensued, Shah Jahan emerged victorious. He put to death all of his rivals for the throne and crowned himself emperor in January 1628 in Agra under the regnal title "Shah Jahan" (which was originally given to him as a princely title). Although an able military commander, Shah Jahan is perhaps best remembered for his architectural achievements. The period of his reign is widely considered to be the golden age of Mughal architecture. Shah Jahan commissioned many monuments, the best known of which is the Taj Mahal in Agra, which entombs his wife Mumtaz Mahal. In September 1657, Shah Jahan fell seriously ill, which set off a war of succession among his four sons, in which his third son Aurangzeb, emerged victorious.[10] Shah Jahan recovered from his illness, but Aurangzeb put his father under house arrest in Agra Fort from July 1658 until his death in January 1666.[11] On 31 July 1658, Aurangzeb crowned himself emperor under the title "Alamgir".[12]'''

    questionList = aqg.aqgParse(inputText)
    # print(questionList)
    WHquestions = aqg.display(questionList)

    #aqg.DisNormal(questionList)

    return WHquestions


# Call Main Function
if __name__ == "__main__":
    HELLO()

