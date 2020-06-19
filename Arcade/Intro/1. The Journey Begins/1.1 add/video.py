from manimlib.imports import *
import numpy as np
from numpy import array as c

class mainScene(Scene):
    def construct(self):
        ######################### # intro
        detail = ['- Intro' ,'- The Journey Begins / add']
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

        detailP = TextMobject(r'\begin{flushleft} Write a function that returns the sum of two numbers. \end{flushleft}')
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

        detailE = TextMobject(r'\begin{flushleft} - For param1 = 1 and param2 = 2 \\ \hspace{0.5cm} the output should be add(param1, param2) = 3. \end{flushleft}')
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

        detailIO = TextMobject(r'\begin{flushleft} - $[$execution time limit$]$ 4 seconds (py3) \\\hspace{0.005cm}- $[$input$]$ integer param1 \\ \hspace{0.5cm} Guaranteed constraints: \\ \hspace{0.7cm} -1000 $\leq$ param1 $\leq$ 1000.\\\hspace{0.005cm}- $[$input$]$ integer param2 \\ \hspace{0.5cm} Guaranteed constraints: \\ \hspace{0.7cm} -1000 $\leq$ param1 $\leq$ 1000. \\\hspace{0.005cm}- $[$output$]$ integer \\ \hspace{5mm}The sum of the two inputs. \end{flushleft}')
        detailIO.scale(0.8)
        detailIO.move_to(title.get_left() - c([(detailIO.get_left()[0] - detailIO.get_right()[0])/2 ,detailIO.get_top()[1] ,0]) + DOWN*1.5 + RIGHT*0.5)

        ###
        self.play(Write(headerIO))
        self.play(Write(detailIO))
        self.wait(0.5)

        self.play(FadeOut(headerIO) ,FadeOut(detailIO))
        ######################### # Solve
        headerS = TextMobject(r'\begin{flushleft} Solve \end{flushleft}')
        headerS.move_to(title.get_left() - headerS.get_left() + DOWN + 0.3*RIGHT)

        detailS1 = TextMobject(r'Input : ' ,r' param1' ,r' , ' ,r'param2')
        detailS2 = TextMobject(r'Output : ' ,r'param1' ,r' + ' ,r'param2').move_to(DOWN)
        # detailS.scale(0.8)
        # detailS.move_to(title.get_left() - c([(detailS.get_left()[0] - detailS.get_right()[0])/2  ,detailS.get_top()[1] ,0]) + DOWN*1.5 + RIGHT*0.5)

        ###
        self.play(Write(headerS))
        self.play(Write(detailS1))
        self.play(Write(detailS2[0]))
        self.play(ReplacementTransform(detailS1[1].copy(),detailS2[1]))
        self.play(Write(detailS2[2]))
        self.play(ReplacementTransform(detailS1[3].copy(),detailS2[3]))
        self.wait(0.5)

        self.play(FadeOut(headerS) ,FadeOut(detailS1), FadeOut(detailS2))
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