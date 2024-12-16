for char in '%20' '%0a' '%00' '%0d0a' '/' '.\\' '.' '…' ':'; do
    for ext in '.php' '.phps' '.php' '.php3' '.php4' '.php5' '.php7' '.php8' '.pht' '.phar' '.phpt' '.pgif' '.phtml' '.phtm'; do
        echo "$char$ext.jpg" >> wordlist.txt
        echo "$ext$char.jpg" >> wordlist.txt
        echo ".jpg$char$ext" >> wordlist.txt
        echo ".jpg$ext$char" >> wordlist.txt
    done
done
