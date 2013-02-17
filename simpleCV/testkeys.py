from SimpleCV import Image
template = Image('wave1.jpg')
img = Image('wave2.jpg')
#match = img.findKeypointMatch(template)
match = img.drawKeypointMatches(template,490.00,0.05)
#drawKeypointMatches()
#match.draw(width=3)
#img.show()
match.save("match.jpg")
match.show()

