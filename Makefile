.PHONY: clean emulate deploy

cloudfn:
	py-cloud-fn scryfall-telegram http -f scryfall_telegram/main.py --python_version 3.5 -v

cloudfn-prod:
	py-cloud-fn scryfall-telegram http -f scryfall_telegram/main.py --python_version 3.5 --production -v

emulate: cloudfn
	cd cloudfn/target && \
	npm install && \
	functions deploy scryfall-telegram --trigger-http && \
	cd ../..

clean:
	rm -r cloudfn

deploy:
	cd cloudfn/target && \
	gcloud beta functions deploy scryfall-telegram --trigger-http --stage-bucket scryfall-telegram --memory 128 && \
	cd ../..
