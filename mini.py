from ytdownloader import *
import json

x = YTDownloader()

data = json.loads(
    """
    {
		"category": "Songs",
		"resultType": "song",
		"title": "Rock the Casbah",
		"album": {
			"name": "Combat Rock",
			"id": "MPREb_zDsyQq5Wq65"
		},
		"feedbackTokens": {
			"add": null,
			"remove": null
		},
		"videoId": "0pCFVX6lzHU",
		"duration": "3:43",
		"year": null,
		"artists": [
			{
				"name": "The Clash",
				"id": "UCf-a_3DiA07vhQmoEaczDhw"
			}
		],
		"isExplicit": false,
		"thumbnails": [
			{
				"url": "https://lh3.googleusercontent.com/75evsI-Mqt8HSD_W1eeXKixhg9Mu_J8OlpBOJ4s86zLZ22c_h7CPbySA95RPJTh6YnqZzTDPN5gFNsY=w60-h60-l90-rj",
				"width": 60,
				"height": 60
			},
			{
				"url": "https://lh3.googleusercontent.com/75evsI-Mqt8HSD_W1eeXKixhg9Mu_J8OlpBOJ4s86zLZ22c_h7CPbySA95RPJTh6YnqZzTDPN5gFNsY=w120-h120-l90-rj",
				"width": 120,
				"height": 120
			}
		]
	}"""
)

x.add_to_queue(data)

x.download()