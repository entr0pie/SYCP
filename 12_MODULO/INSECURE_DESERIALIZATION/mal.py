class Evil:
	def __reduce__(self):
		return (print, ("hi",))
