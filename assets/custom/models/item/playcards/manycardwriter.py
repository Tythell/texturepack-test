format = '''{
	"parent": "custom:item/playcards/cardparent",
	"textures": {
		"0":  "custom:item/playcards/%s"
	}
}'''

for suit in ["spade", "heart", "club", "diamond"]:
    for num in range(1,14):
        card = suit + str(num)
        with open(card + str(".json"), 'w') as writer:
            writer.write(format % card)
