import wx
import random
import time
import threading

class MyPanel(wx.Panel):


    def __init__(self, parent):
        super().__init__(parent)
        self.mode = 1
        self.math_button_size = (parent.size[0]/4, parent.size[1]/4)
        self.add_button = wx.Button(self, label="Addition", size=self.math_button_size)
        self.add_button.Bind(wx.EVT_BUTTON, self.addition)
        self.sub_button = wx.Button(self, label="Subtraction", size=self.math_button_size)
        self.sub_button.Bind(wx.EVT_BUTTON, self.subtraction)
        self.mul_button = wx.Button(self, label="Multiplication", size=self.math_button_size)
        self.mul_button.Bind(wx.EVT_BUTTON, self.multiplication)
        self.div_button = wx.Button(self, label="Division", size=self.math_button_size)
        self.div_button.Bind(wx.EVT_BUTTON, self.division)
        self.main_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.mode_sizer = wx.BoxSizer(wx.VERTICAL)

        self.mode_font = self.add_button.GetFont()
        self.mode_font.PointSize+=15
        self.add_button.SetFont(self.mode_font)
        self.sub_button.SetFont(self.mode_font)
        self.mul_button.SetFont(self.mode_font)
        self.div_button.SetFont(self.mode_font)

        self.mode_sizer.Add(self.add_button, proportion=1,
                        flag = wx.ALL | wx.CENTER | wx.EXPAND,
                        border=0)
        self.mode_sizer.Add(self.sub_button, proportion=1,
                        flag = wx.ALL | wx.CENTER | wx.EXPAND,
                        border=0)
        self.mode_sizer.Add(self.mul_button, proportion=1,
                        flag = wx.ALL | wx.CENTER | wx.EXPAND,
                        border=0)
        self.mode_sizer.Add(self.div_button, proportion=1,
                        flag = wx.ALL | wx.CENTER | wx.EXPAND,
                        border=0)
        self.main_sizer.Add(self.mode_sizer)


        self.add_top = 1
        self.add_bottom = 1
        self.sub_top = 1
        self.sub_bottom = 1
        self.mul_top = 1
        self.mul_bottom = 1
        self.div_top = 1
        self.div_bottom = 1

        self.answer_given = 0
        self.actual_answer = 'foo'

        self.start_time = 0
        self.finish_time = 0
        self.time_elapsed = 0

        self.session_data = {"Date": time.asctime(time.localtime(time.time())), "Questions": []}

        self.top_bottom_sizer = wx.BoxSizer(wx.VERTICAL)

        self.top_bottom_size = (parent.size[0]/16, parent.size[1]/8)
        #self.add_top_box = wx.StaticBox(self, size=self.top_bottom_size)
        self.add_top_text = wx.StaticText(self, label="1",size = self.top_bottom_size, style=wx.ALIGN_CENTER)
        self.font = self.add_top_text.GetFont()
        self.font.PointSize+=30
        self.font = self.font.Bold()
        self.add_top_text.SetFont(self.font)
        self.top_bottom_sizer.Add(self.add_top_text, proportion=1,
                                flag = wx.ALL | wx.CENTER | wx.EXPAND, border=0)

        #self.add_bottom_box = wx.StaticBox(self, size=self.top_bottom_size)
        self.add_bottom_text = wx.StaticText(self,size = self.top_bottom_size, label="1", style=wx.ALIGN_CENTER)
        self.add_bottom_text.SetFont(self.font)
        self.top_bottom_sizer.Add(self.add_bottom_text, proportion=1,
                                flag = wx.ALL | wx.CENTER | wx.EXPAND, border=0)

        #self.sub_top_box = wx.StaticBox(self, size=self.top_bottom_size)
        self.sub_top_text = wx.StaticText(self,size = self.top_bottom_size, label="1", style=wx.ALIGN_CENTER)
        self.sub_top_text.SetFont(self.font)
        self.top_bottom_sizer.Add(self.sub_top_text, proportion=1,
                                flag = wx.ALL | wx.CENTER | wx.EXPAND, border=0)

        #self.sub_bottom_box = wx.StaticBox(self, size=self.top_bottom_size)
        self.sub_bottom_text = wx.StaticText(self,size = self.top_bottom_size, label="1", style=wx.ALIGN_CENTER)
        self.sub_bottom_text.SetFont(self.font)
        self.top_bottom_sizer.Add(self.sub_bottom_text, proportion=1,
                                flag = wx.ALL | wx.CENTER | wx.EXPAND, border=0)

        #self.mul_top_box = wx.StaticBox(self, size=self.top_bottom_size)
        self.mul_top_text = wx.StaticText(self,size = self.top_bottom_size, label="1", style=wx.ALIGN_CENTER)
        self.mul_top_text.SetFont(self.font)
        self.top_bottom_sizer.Add(self.mul_top_text, proportion=1,
                                flag = wx.ALL | wx.CENTER | wx.EXPAND, border=0)

        #self.mul_bottom_box = wx.StaticBox(self, size=self.top_bottom_size)
        self.mul_bottom_text =wx.StaticText(self,size = self.top_bottom_size, label="1", style=wx.ALIGN_CENTER)
        self.mul_bottom_text.SetFont(self.font)
        self.top_bottom_sizer.Add(self.mul_bottom_text, proportion=1,
                                flag = wx.ALL | wx.CENTER | wx.EXPAND, border=0)

        #self.div_top_box = wx.StaticBox(self, size=self.top_bottom_size)
        self.div_top_text = wx.StaticText(self,size = self.top_bottom_size, label="1", style=wx.ALIGN_CENTER)
        self.div_top_text.SetFont(self.font)
        self.top_bottom_sizer.Add(self.div_top_text, proportion=1,
                                flag = wx.ALL | wx.CENTER | wx.EXPAND, border=0)

        #self.div_bottom_box = wx.StaticBox(self, size=self.top_bottom_size)
        self.div_bottom_text = wx.StaticText(self,size = self.top_bottom_size, label="1", style=wx.ALIGN_CENTER)
        self.div_bottom_text.SetFont(self.font)
        self.top_bottom_sizer.Add(self.div_bottom_text, proportion=1,
                                flag = wx.ALL | wx.CENTER | wx.EXPAND, border=0)

        self.main_sizer.Add(self.top_bottom_sizer)

        self.ticker_sizer = wx.BoxSizer(wx.VERTICAL)
        self.ticker_button_size = (parent.size[0]/32, parent.size[1]/16)
        # up_arrow = wx.Bitmap('up_arrow_3.png')
        self.add_top_up = wx.Button(self,label="/\\", size=self.ticker_button_size)
        # add_top_up.SetBitmap(up_arrow)
        self.add_top_up.Bind(wx.EVT_BUTTON, self.addTopUp)
        self.ticker_sizer.Add(self.add_top_up, proportion=1,
                            flag = wx.ALL | wx.CENTER | wx.EXPAND, border=0)

        self.add_top_down = wx.Button(self,label="\\/", size=self.ticker_button_size)
        self.add_top_down.Bind(wx.EVT_BUTTON, self.addTopDown)
        self.ticker_sizer.Add(self.add_top_down, proportion=1,
                            flag = wx.ALL | wx.CENTER | wx.EXPAND, border=0)
        self.add_bottom_up = wx.Button(self,label="/\\", size=self.ticker_button_size)
        self.add_bottom_up.Bind(wx.EVT_BUTTON, self.addBottomUp)
        self.ticker_sizer.Add(self.add_bottom_up, proportion=1,
                            flag = wx.ALL | wx.CENTER | wx.EXPAND, border=0)
        self.add_bottom_down = wx.Button(self,label="\\/", size=self.ticker_button_size)
        self.add_bottom_down.Bind(wx.EVT_BUTTON, self.addBottomDown)
        self.ticker_sizer.Add(self.add_bottom_down, proportion=1,
                            flag = wx.ALL | wx.CENTER | wx.EXPAND, border=0)


        self.sub_top_up = wx.Button(self,label="/\\", size=self.ticker_button_size)
        self.sub_top_up.Bind(wx.EVT_BUTTON, self.subTopUp)
        self.ticker_sizer.Add(self.sub_top_up, proportion=1,
                            flag = wx.ALL | wx.CENTER | wx.EXPAND, border=0)
        self.sub_top_down = wx.Button(self,label="\\/", size=self.ticker_button_size)
        self.sub_top_down.Bind(wx.EVT_BUTTON, self.subTopDown)
        self.ticker_sizer.Add(self.sub_top_down, proportion=1,
                            flag = wx.ALL | wx.CENTER | wx.EXPAND, border=0)
        self.sub_bottom_up = wx.Button(self,label="/\\", size=self.ticker_button_size)
        self.sub_bottom_up.Bind(wx.EVT_BUTTON, self.subBottomUp)
        self.ticker_sizer.Add(self.sub_bottom_up, proportion=1,
                            flag = wx.ALL | wx.CENTER | wx.EXPAND, border=0)
        self.sub_bottom_down = wx.Button(self,label="\\/", size=self.ticker_button_size)
        self.sub_bottom_down.Bind(wx.EVT_BUTTON, self.subBottomDown)
        self.ticker_sizer.Add(self.sub_bottom_down, proportion=1,
                            flag = wx.ALL | wx.CENTER | wx.EXPAND, border=0)

        self.mul_top_up = wx.Button(self,label="/\\", size=self.ticker_button_size)
        self.mul_top_up.Bind(wx.EVT_BUTTON, self.mulTopUp)
        self.ticker_sizer.Add(self.mul_top_up, proportion=1,
                            flag = wx.ALL | wx.CENTER | wx.EXPAND, border=0)
        self.mul_top_down = wx.Button(self,label="\\/", size=self.ticker_button_size)
        self.mul_top_down.Bind(wx.EVT_BUTTON, self.mulTopDown)
        self.ticker_sizer.Add(self.mul_top_down, proportion=1,
                            flag = wx.ALL | wx.CENTER | wx.EXPAND, border=0)
        self.mul_bottom_up = wx.Button(self, label="/\\",size=self.ticker_button_size)
        self.mul_bottom_up.Bind(wx.EVT_BUTTON, self.mulBottomUp)
        self.ticker_sizer.Add(self.mul_bottom_up, proportion=1,
                            flag = wx.ALL | wx.CENTER | wx.EXPAND, border=0)
        self.mul_bottom_down = wx.Button(self,label="\\/", size=self.ticker_button_size)
        self.mul_bottom_down.Bind(wx.EVT_BUTTON, self.mulBottomDown)
        self.ticker_sizer.Add(self.mul_bottom_down, proportion=1,
                            flag = wx.ALL | wx.CENTER | wx.EXPAND, border=0)

        self.div_top_up = wx.Button(self,label="/\\", size=self.ticker_button_size)
        self.div_top_up.Bind(wx.EVT_BUTTON, self.divTopUp)
        self.ticker_sizer.Add(self.div_top_up, proportion=1,
                            flag = wx.ALL | wx.CENTER | wx.EXPAND, border=0)
        self.div_top_down = wx.Button(self,label="\\/", size=self.ticker_button_size)
        self.div_top_down.Bind(wx.EVT_BUTTON, self.divTopDown)
        self.ticker_sizer.Add(self.div_top_down, proportion=1,
                            flag = wx.ALL | wx.CENTER | wx.EXPAND, border=0)
        self.div_bottom_up = wx.Button(self,label="/\\", size=self.ticker_button_size)
        self.div_bottom_up.Bind(wx.EVT_BUTTON, self.divBottomUp)
        self.ticker_sizer.Add(self.div_bottom_up, proportion=1,
                            flag = wx.ALL | wx.CENTER | wx.EXPAND, border=0)
        self.div_bottom_down = wx.Button(self, label="\\/",size=self.ticker_button_size)
        self.div_bottom_down.Bind(wx.EVT_BUTTON, self.divBottomDown)
        self.ticker_sizer.Add(self.div_bottom_down, proportion=1,
                            flag = wx.ALL | wx.CENTER | wx.EXPAND, border=0)
        self.main_sizer.Add(self.ticker_sizer)


        self.answer_window_sizer = wx.BoxSizer(wx.VERTICAL)

        self.sign_and_question_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.test = "---\n---"
        # question_box = wx.StaticBox(self, size=(21*parent.size[0]/32, 3*parent.size[1]/4))
        self.sign_text = wx.StaticText(self,-1,"+",
                                        size=(10*parent.size[0]/32,
                                        3*parent.size[1]/4),
                                        style=wx.ALIGN_CENTER)
        self.sfont = self.sign_text.GetFont()
        self.sfont.PointSize+=200
        #self.sfont = self.sfont.Bold()
        self.sign_text.SetFont(self.sfont)
        self.question_text = wx.StaticText(self,-1,self.test,
                                        size=(11*parent.size[0]/32,
                                        3*parent.size[1]/4),
                                        style=wx.ALIGN_RIGHT)
        self.qfont = self.question_text.GetFont()
        self.qfont.PointSize+=90
        self.qfont = self.qfont.Bold()
        self.question_text.SetFont(self.qfont)
        self.sign_and_question_sizer.Add(self.sign_text, proportion=1,
                                flag = wx.ALL | wx.CENTER | wx.EXPAND, border=0)
        self.sign_and_question_sizer.Add(self.question_text, proportion=1,
                                flag = wx.ALL | wx.CENTER | wx.EXPAND, border=0)
        self.answer_window_sizer.Add(self.sign_and_question_sizer)

        self.answer_bar_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.status = wx.StaticText(self,-1,"",size=(10*parent.size[0]/32,
                                    parent.size[1]/4), style=wx.ALIGN_CENTER )
        self.status.SetFont(self.font)

        self.answer_input = wx.TextCtrl(self, value="", size = (11*parent.size[0]/32,
                                    parent.size[1]/4), style=wx.TE_RIGHT)
        self.answer_input.SetFont(self.font)
        """ Need to decide whether to use the ENTER button as a trigger
        or the changing of text. Enter would allow for the tracking of time and
        right/wrong but text-change would allow for faster training. Gonna start
        with changing of text. Making a commit here """
        self.answer_input.Bind(wx.EVT_TEXT, self.answerTextChange)
        self.answer_bar_sizer.Add(self.status, proportion=1,
                                flag = wx.ALL | wx.CENTER | wx.EXPAND, border=0)
        self.answer_bar_sizer.Add(self.answer_input, proportion=1,
                                flag = wx.ALL | wx.CENTER | wx.EXPAND, border=0)
        self.answer_window_sizer.Add(self.answer_bar_sizer)
        self.main_sizer.Add(self.answer_window_sizer)
        self.SetSizer(self.main_sizer)

        #Maybe have the mode buttons give you a single question and then the
         # enter button could give you a new problem by re-calling it

    def addition(self, event):
        self.start_time = time.perf_counter()
        self.mode = 1
        self.sign_text.SetLabel("+")
        self.top_number = random.randrange(10**(self.add_top-1), 10**(self.add_top))
        self.bottom_number = random.randrange(10**(self.add_bottom-1), 10**(self.add_bottom))
        self.question_text.SetLabel(str(self.top_number) + "\n" + str(self.bottom_number))
        self.actual_answer = str(self.top_number + self.bottom_number)

    def subtraction(self, event): #ensures bottom number is smaller
        self.start_time = time.perf_counter()
        self.mode = 2
        self.sign_text.SetLabel("-")
        self.top_number = random.randrange(10**(self.sub_top-1), 10**(self.sub_top))
        self.bottom_number = random.randrange(10**(self.sub_bottom-1), min([self.top_number, 10**(self.sub_bottom)]))
        self.question_text.SetLabel(str(self.top_number) + "\n" + str(self.bottom_number))
        self.actual_answer = str(self.top_number - self.bottom_number)

    def multiplication(self, event):
        self.start_time = time.perf_counter()
        self.mode = 3
        self.sign_text.SetLabel("*")
        self.top_number = random.randrange(10**(self.mul_top-1), 10**(self.mul_top))
        self.bottom_number = random.randrange(10**(self.mul_bottom-1), 10**(self.mul_bottom))
        self.question_text.SetLabel(str(self.top_number) + "\n" + str(self.bottom_number))
        self.actual_answer = str(self.top_number * self.bottom_number)

    def division(self, event): #TODO: no control currently - but maybe add divisor selection
        # You could maybe do a slider from 0 - 1000 to pick sizes instead of digit counts
        self.start_time = time.perf_counter()
        self.mode = 4
        self.sign_text.SetLabel("/")
        self.top_number = random.randrange(10**(self.div_top-1), 10**(self.div_top))
        self.bottom_number = random.randrange(10**(self.div_bottom-1), 10**(self.div_bottom))
        self.question_text.SetLabel(str(self.top_number) + "\n" + str(self.bottom_number))
        ans = round(self.top_number/self.bottom_number, 2)
        if int(ans) - ans == 0:
            self.actual_answer = str(int(ans))
        else:
            self.actual_answer = str(round(self.top_number/self.bottom_number, 2))

    def addTopUp(self, event):
        self.add_top += 1
        self.add_top_text.SetLabel(str(self.add_top))

    def addTopDown(self, event):
        self.add_top -= 1
        if self.add_top < 1:
            self.add_top = 1
        self.add_top_text.SetLabel(str(self.add_top))

    def addBottomUp(self, event):
        self.add_bottom += 1
        self.add_bottom_text.SetLabel(str(self.add_bottom))

    def addBottomDown(self, event):
        self.add_bottom -= 1
        if self.add_bottom < 1:
            self.add_bottom = 1
        self.add_bottom_text.SetLabel(str(self.add_bottom))

    def subTopUp(self, event):
        self.sub_top += 1
        self.sub_top_text.SetLabel(str(self.sub_top))

    def subTopDown(self, event):
        self.sub_top -= 1
        if self.sub_top < 1:
            self.sub_top = 1
        self.sub_top_text.SetLabel(str(self.sub_top))

    def subBottomUp(self, event):
        self.sub_bottom += 1
        self.sub_bottom_text.SetLabel(str(self.sub_bottom))

    def subBottomDown(self, event):
        self.sub_bottom -= 1
        if self.sub_bottom < 1:
            self.sub_bottom = 1
        self.sub_bottom_text.SetLabel(str(self.sub_bottom))

    def mulTopUp(self, event):
        self.mul_top += 1
        self.mul_top_text.SetLabel(str(self.mul_top))

    def mulTopDown(self, event):
        self.mul_top -= 1
        if self.mul_top < 1:
            self.mul_top = 1
        self.mul_top_text.SetLabel(str(self.mul_top))

    def mulBottomUp(self, event):
        self.mul_bottom += 1
        self.mul_bottom_text.SetLabel(str(self.mul_bottom))

    def mulBottomDown(self, event):
        self.mul_bottom -= 1
        if self.mul_bottom < 1:
            self.mul_bottom = 1
        self.mul_bottom_text.SetLabel(str(self.mul_bottom))

    def divTopUp(self, event):
        self.div_top += 1
        self.div_top_text.SetLabel(str(self.div_top))

    def divTopDown(self, event):
        self.div_top -= 1
        if self.div_top < 1:
            self.div_top = 1
        self.div_top_text.SetLabel(str(self.div_top))

    def divBottomUp(self, event):
        self.div_bottom += 1
        self.div_bottom_text.SetLabel(str(self.div_bottom))

    def divBottomDown(self, event):
        self.div_bottom -= 1
        if self.div_bottom < 1:
            self.div_bottom = 1
        self.div_bottom_text.SetLabel(str(self.div_bottom))

    def answerTextChange(self, event):
        self.answer_given = self.answer_input.GetLineText(0)
        if len(self.answer_given) == 0:
            return
        if len(self.answer_given) >= 1:
            if self.answer_given[-1]==".":
                return
            if (not self.answer_given[-1].isdigit()):
                temp = self.answer_given[:-1]
                self.answer_input.Clear()
                self.answer_input.write(temp)
        if self.answer_given == self.actual_answer: #Correct answer given
            self.finish_time = time.perf_counter()
            self.time_elapsed = round(self.finish_time-self.start_time, 2)
            #print(self.time_elapsed) #TODO: Figure out how best to store session data
            self.session_data["Questions"].append((self.time_elapsed, self.mode,
                                                len(str(self.top_number)),
                                                len(str(self.bottom_number)),
                                                self.top_number, self.bottom_number))
            self.answer_input.Clear()
            self.status.SetLabel("Correct!")
            x = threading.Thread(target=self.correctText, daemon=True)
            x.start()
            if self.mode == 1:
                self.addition(wx.EVT_BUTTON) #These functions should start the player timer
            elif self.mode == 2:
                self.subtraction(wx.EVT_BUTTON)
            elif self.mode == 3:
                self.multiplication(wx.EVT_BUTTON)
            else:
                self.division(wx.EVT_BUTTON)

    def correctText(self):
        time.sleep(0.5)
        self.status.SetLabel("")

    def exportSessionData(self):
        with open("history.txt", "a") as f:
            f.write(self.session_data["Date"])
            f.write("\n\n")
            f.write("Time\tMode\tTop\tBottom\tTop\tBottom\n")
            for question in self.session_data["Questions"]:
                for element in question:
                    f.write(str(element))
                    f.write("\t")
                f.write("\n")


#TODO: You made this code to hopefully write your session data to a file
#TODO: You need to make this run when the application is closed somehow and then debug it.

class MainFrame(wx.Frame):
    size = (1024,512)

    def __init__(self):
        super().__init__(None, title="Math Trainer", size=self.size)
        self.Bind(wx.EVT_CLOSE, self._when_closed)
        self.panel = MyPanel(self)
        self.Show()

    def _when_closed(self, event):
        self.panel.exportSessionData()
        self.Destroy()

if __name__ == "__main__":
    app = wx.App(redirect=False)
    frame = MainFrame()
    app.MainLoop()
