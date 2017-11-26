.PHONY: clean emulate

cloudfn:
	py-cloud-fn scryfall-telegram http -f scryfall_telegram/main.py --python_version 3.5 && \
	cp endpoint.txt cloudfn/target/dist/func/ && cp token.txt cloudfn/target/dist/func/

emulate: cloudfn
	cd cloudfn/target && npm install && functions deploy scryfall-telegram --trigger-http && cd ../..

clean:
	rm -r cloudfn
