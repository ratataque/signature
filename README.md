# Signature asymétrique test#

Bonjour pour utiliser mes programmes il suffit soit d'importer votre private key sous le nom "private.pem" ou en creer une avec cette commande dans un shell linux en étant ici "signature/signatest/":

<pre>
    <code>openssl genrsa -out private.pem 2048</code>
</pre>

sinon le programme générera une clé privé automatiquement.
<br>
Ensuite écrivez ce que vous voulez dans message.txt et lancez Signe.py
<br>
<br>
Après pour vérifier la signature, lancez Verif.py.
Et voila