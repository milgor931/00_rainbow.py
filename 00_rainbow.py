def write_colorful_text(string, style, foreground, background):
  s1 = ""
  for i in string:
    format = ';'.join([str(style), str(foreground), str(background)])
    s1 += '\x1b[%sm %s \x1b[0m' % (format, i)
    if style < 8:
      style += 1
    else:
      style = 0
    if foreground < 38:
      foreground += 1
    else:
      foreground = 30
    if background < 48:
      background += 1
    else:
      background = 40
  print(s1)
write_colorful_text("RAINBOW", 3, 32, 45)
