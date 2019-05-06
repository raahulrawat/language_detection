# language detection using Google's language detection library
from langdetect import detect
master_check = {"af": "Afrikaans", "ar": "Arabic", "bg":"Bulgarian", "bn": "Bengali", "ca":"Catalan", "cs":"Czech", "cy":"Welsh", "da":"Danish", "de":"German", "el":"Greek", "en":"English", "es":"", "et":"Estonian", "fa":"Persian", "fi":"Finnish", "fr":"French", "gu":"Gujarati", "he":'Hebrew',
"hi":"Hindi", "hr":"Croatian", "hu":"Hungarian", "id":"Indonesian", "it":"Italian", "ja":"Japanese", "kn":"Kannada", "ko":"Korean", "lt":"Lithuanian", "lv":"Latvian", "mk":"Macedonian", "ml":"Malayalam", "mr":"Marathi", "ne":'Nepali', "nl":"Dutch", "no":"Norwegian", "pa":"Punjabi", "pl":"Polish",
"pt":"Portuguese", "ro":"Romanian", "ru":"Russian", "sk":"Slovak", "sl":"Slovenian", "so":"Somali", "sq":"Albanian", "sv":"Swedish", "sw":"Swahili", "ta":"Tamil", "te":"Telugu", "th":"Thai", "tl":"Filipino", "tr":"Turkish", "uk":"Ukrainian", "ur":"Urdu", "vi":"Vietnamese", "zh-cn":"Chinese (Simplified)", "zh-tw":"Chinese (Traditional)"}

lang = detect("War doesn't show who's right, just who's left.")
detectedLang = master_check[lang]
print(detectedLang)
