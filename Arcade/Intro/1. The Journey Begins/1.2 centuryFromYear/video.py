from manimlib.imports import *
import numpy as np
from numpy import array as c

class mainScene(Scene):
    def construct(self):
        ######################### # intro
        detail = ['- Intro' ,'- The Journey Begins / centuryFromYear']
        detailShift = [[3.5 ,3.5],[3.45 , 3.05]]

        title = TextMobject('CodeSignal ')
        title.scale(5)
        titleDetail = [TextMobject(i).scale(0.7) for i in detail]
        
        lineS = c([-6.5 ,2.7 ,0])
        lineE = c([ 6.5 ,2.7 ,0])
        
        ###
        self.wait(0.5)
        self.play(Write(title))
        self.wait(0.5)
        self.play(title.scale, 0.23, title.to_corner, UL, run_time=2)

        for i in enumerate(titleDetail):
            i[1].move_to(-i[1].get_left() + detailShift[0][i[0]] * LEFT + detailShift[1][i[0]] * UP)
        
        self.wait(0.5)
        
        for i in  titleDetail:
            self.play(Write(i))
        self.wait(0.5)

        line = Line(lineS,lineE)
        self.play(ShowCreation(line))

        ######################### # Proposition
        headerP = TextMobject(r'Proposition')
        headerP.move_to(title.get_left() - headerP.get_left() + DOWN + 0.3*RIGHT)

        detailP = TextMobject(r'\begin{flushleft} Given a year, return the century it is in.The first century spans from \\ the year 1 up to and including the year 100, the second - from the year \\ 101 up to and including the year 200, etc. \end{flushleft}')
        detailP.scale(0.8)
        detailP.move_to(title.get_left() - c([(detailP.get_left()[0] - detailP.get_right()[0])/2  ,detailP.get_top()[1] ,0]) + DOWN*1.5 + RIGHT*0.5)

        ###
        self.play(Write(headerP))
        self.play(Write(detailP))
        self.wait(0.5)
        self.play(FadeOut(headerP) ,FadeOut(detailP))

        ######################### # Example
        headerE = TextMobject(r'\begin{flushleft} Example \end{flushleft}')
        headerE.move_to(title.get_left() - headerE.get_left() + DOWN + 0.3*RIGHT)

        detailE = TextMobject(r'\begin{flushleft}- For year = 1905, the output should be\\\hspace{0.5cm}centuryFromYear(year) = 20;\\- For year = 1700, the output should be\\\hspace{0.5cm}centuryFromYear(year) = 17.\\ \end{flushleft}')
        detailE.scale(0.8)
        detailE.move_to(title.get_left() - c([(detailE.get_left()[0] - detailE.get_right()[0])/2 ,detailE.get_top()[1] ,0]) + DOWN*1.5 + RIGHT*0.5)

        ###
        self.play(Write(headerE))
        self.play(Write(detailE))
        self.wait(0.5)

        self.play(FadeOut(headerE) ,FadeOut(detailE))

        ######################### # Input/Output
        headerIO = TextMobject(r'\begin{flushleft} Input/Output \end{flushleft}')
        headerIO.move_to(title.get_left() - headerIO.get_left() + DOWN + 0.3*RIGHT)

        detailIO = TextMobject(r'\begin{flushleft} - $[$execution time limit$]$ 4 seconds (py3) \\\hspace{0.005cm}- $[$input$]$ integer year\\\hspace{0.5cm}A positive integer, designating the year.\\\hspace{0.5cm}Guaranteed constraints:\\\hspace{1cm}1 $\leq$ year $\leq$ 2005.\\\hspace{0.005cm}- $[$output$]$ integer\\\hspace{0.5cm}The number of the century the year is in. \end{flushleft}')
        detailIO.scale(0.8)
        detailIO.move_to(title.get_left() - c([(detailIO.get_left()[0] - detailIO.get_right()[0])/2 ,detailIO.get_top()[1] ,0]) + DOWN*1.5 + RIGHT*0.5)

 
        ###
        self.play(Write(headerIO))
        self.play(Write(detailIO))
        self.wait(0.5)

        self.play(FadeOut(headerIO) ,FadeOut(detailIO))
        ######################### # Solve
        headerS = TextMobject(r'\begin{flushleft} Solve 1 \end{flushleft}')
        headerS.move_to(title.get_left() - headerS.get_left() + DOWN + 0.3*RIGHT)

        detailS1 = TextMobject(r'Input : 1907').move_to(UP*1.5 + LEFT * 3) 
        detailS12 = TextMobject(r'Output : 1907 // 100 + if 07 $\neq$ 00 then 1 else 0')
        detailS12.move_to(DOWN*1 + detailS1.get_left() - detailS12.get_left())
        
        detailS2 = TextMobject(r'Input : 1700').move_to(DOWN*0.5 + LEFT * 3)
        detailS22 = TextMobject(r'Output : 1700 // 100 + if 00 $\neq$ 00 then 1 else 0')
        detailS22.move_to(DOWN*1 + detailS2.get_left() - detailS22.get_left())
        # detailS.scale(0.8)
        # detailS.move_to(title.get_left() - c([(detailS.get_left()[0] - detailS.get_right()[0])/2  ,detailS.get_top()[1] ,0]) + DOWN*1.5 + RIGHT*0.5)
        ###
        self.play(Write(headerS))
        self.play(Write(detailS1))
        self.play(Write(detailS12[0][:7]))
        self.play(ReplacementTransform(detailS1[0][6:].copy(), detailS12[0][7:11]))


        self.play(ReplacementTransform(detailS12,detailS12)) 
        self.play(ShowCreation(Line(c([-6.5,0,0]), c([6.5,0,0]))))
        self.play(Write(detailS2))
        self.play(Write(detailS22))
        
        # self.play(Write(detailS2[2]))
        # self.play(ReplacementTransform(detailS1[3].copy(),detailS2[3]))
        self.wait(0.5)

        # self.play(FadeOut(headerS) ,FadeOut(detailS1), FadeOut(detailS2))
        ######################### # Coding
        headerC = TextMobject(r'Coding')
        headerC.move_to(title.get_left() - headerC.get_left() + DOWN + 0.3*RIGHT)

        detailC = Code( r"answer.py",
                        insert_line_no=False,
                        font = 'Courier New',
                        tab_width=4,
                        language=code_languages_list["python"])
        # detailColor = []
        detailC.scale(1.5)
        detailC.move_to(title.get_left() - c([(detailC.get_left()[0] - detailC.get_right()[0])/2  ,detailC.get_top()[1] ,0]) + DOWN*1.5 + RIGHT*0.5)

        ###
        self.play(Write(headerC))
        self.play(Write(detailC))
        self.wait(0.5)
        # self.play(FadeOut(headerC) ,FadeOut(detailC))

        self.wait(5)