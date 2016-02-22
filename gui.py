from backend import *
    
class GUI():
	SELECTED_COLOR = None;
	def __init__(self):
        
#		p = Gsettings('palette')
		self.p = Palette()
		self.buttons ={}
		root =Tk()
		root.title('colorTerminal')
        #root.columnconfigure(0, weight=1)
        #root.rowconfigure(0, weight=1)
        #root.resizable(width=FALSE,height=FALSE)
		root.geometry('-{}+{}'.format(100, 100))
		"""
		wiFg = Frame(root)
		wiFg.pack()
		wiCursor = Frame(root)
		wiCursor.pack()
		"""
		wiPalette = Frame(root)
		wiPalette.pack(side=LEFT)
        
		separator = Frame(root, width=2, bd=1, relief=SUNKEN)
		separator.pack(fill=Y, side=LEFT, padx=5)
        
		wiBg = Frame(root)
		wiBg.pack(expand=1, fill=BOTH, side=LEFT)
        
		row_col_length = self.setColRow(len(self.p.value))
		print "value {}".format(self.p.value[0])

    
#       Window color selected
		Label(wiBg, text="color selected", justify="center").pack(expand=0, fill=Y)
		self.button_color_selected = Button(wiBg, height=4, width=12, text="..")
		self.button_color_selected.pack(fill=BOTH)
#       Window palette, contains buttons
		Label(wiPalette, text="Palette:", justify="center").grid(row=0, columnspan=row_col_length[1])
		for id, c  in enumerate(self.p.value):
			print id
			self.buttons[id] = Button(wiPalette,height=4, width=12, text="{}\n {}".format(id, c),bg=c,command=lambda id=id: self.pressed(id),borderwidth=.001)
			self.buttons[id].grid(sticky=N+S+E+W, row=id%row_col_length[0]+1,column=int(id/row_col_length[0]))
			self.buttons[id].bind("<Button-3>",self.select_color)

		for x in range(row_col_length[0]):
			Grid.columnconfigure(wiPalette, x, weight=1)
		for y in range(len(self.p.value)/row_col_length[0]):
			Grid.rowconfigure(wiPalette, y, weight=1)
    
		root.mainloop()
			
	def select_color(self, event):
		self.SELECTED_COLOR = event.widget.cget('bg')
		self.button_color_selected.configure(bg=self.SELECTED_COLOR, text=self.SELECTED_COLOR)
	def pressed(self, index):
		self.p.setPalette(index, self.SELECTED_COLOR)
		print self.p.value[index]
		self.buttons[index].configure(bg=self.p.value[index])
	def norme(self, a, b):
		return math.sqrt(a*a+b*b)

	def setColRow(self, L):
		listPotentialColSize = [L%i for i in range(1, L+1)]
		tmpValue = 1000
		print L
		for i in range(1,L+1):
			if listPotentialColSize[i-1] == 0 and self.norme(L/i,i) < tmpValue :
				tmpValue = self.norme(L/i, i)
				tmpIndex = i
		return (tmpIndex, L/tmpIndex)
    
        
init = GUI()
