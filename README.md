```markdown
# Telegram Bot Tutorial

Un bot Telegram simple et éducatif construit avec Python et la bibliothèque `python-telegram-bot`. Ce projet démontre les fonctionnalités de base d'un bot Telegram, y compris les commandes, les menus interactifs et la gestion des messages.

## ✨ Fonctionnalités

- **Commandes de base** :
  - `/start` - Démarrer le bot
  - `/menu` - Afficher un menu interactif avec boutons
  - `/scream` - Activer le mode "cri" (messages en majuscules)
  - `/whisper` - Désactiver le mode "cri"

- **Menu interactif** :
  - Navigation entre différents menus
  - Boutons inline avec callback
  - Lien vers la documentation Telegram Bot API

- **Gestion des messages** :
  - Echo des messages utilisateur
  - Mode "cri" optionnel
  - Préservation du formatage des messages

## 🚀 Démarrage rapide

### Prérequis

- Python 3.11 ou version ultérieure
- Un token de bot Telegram (obtenu via [@BotFather](https://t.me/BotFather))

### Installation

1. **Cloner le repository** :
```bash
git clone https://github.com/votre-username/TelegramBot.git
cd TelegramBot
```

2. **Créer un environnement virtuel** :

```bash
python -m venv .venv
source .venv/bin/activate  # Sur Windows: .venv\Scripts\activate
```

3. **Installer les dépendances** :

```bash
pip install python-telegram-bot
```

4. **Configurer le token du bot** :

   Option A - Variable d'environnement :

```bash
export TELEGRAM_BOT_TOKEN="votre_token_bot_ici"
```

   Option B - Modifier directement le code :
   Éditez `TelegramBot.py` et remplacez `"<YOUR_BOT_TOKEN_HERE>"` par votre token. dans un fichier .env

5. **Lancer le bot** :

```bash
python TelegramBot.py
```

## 🛠 Structure du projet

```
TelegramBot/
├── TelegramBot.py                 # Code principal du bot
├── requirements.txt       # Dépendances Python
├── README.md             # Ce fichier
└── .gitignore           # Fichiers à ignorer par Git
```

## 📋 Commandes disponibles

| Commande | Description |
|----------|-------------|
| `/start` | Démarrer une conversation avec le bot |
| `/menu` | Afficher le menu interactif principal |
| `/scream` | Activer le mode cri (messages en majuscules) |
| `/whisper` | Désactiver le mode cri |

## 🔧 Développement

### Architecture du code

Le bot utilise le pattern asynchrone de `python-telegram-bot` v21.x :

- **Application** : Point d'entrée principal du bot
- **Handlers** : Gestionnaires pour différentes commandes et messages
- **Callbacks** : Gestion des interactions avec les boutons inline

### Ajouter de nouvelles commandes

1. Créer une fonction async :

```python
async def nouvelle_commande(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Réponse de la commande")
```

2. Enregistrer le handler :

```python
application.add_handler(CommandHandler("nouvelle", nouvelle_commande))
```

### Ajouter des boutons interactifs

```python
keyboard = InlineKeyboardMarkup([
    [InlineKeyboardButton("Texte", callback_data="data_callback")]
])
```

## 🌐 Déploiement

### Déploiement local

```bash
uv run TelegramBot.py
```

### Déploiement avec Docker (optionnel)

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "bot.py"]
```

## 📚 Ressources utiles

- [Documentation python-telegram-bot](https://python-telegram-bot.org/)
- [API Telegram Bots](https://core.telegram.org/bots/api)
- [Créer un bot avec BotFather](https://t.me/BotFather)

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :

1. Fork le projet
2. Créer une branche feature (`git checkout -b feature/AmazingFeature`)
3. Commit vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Push sur la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## 📝 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## ⚠️ Notes importantes

- Ne commitez jamais votre token de bot dans le code
- Utilisez des variables d'environnement pour les données sensibles
- Le bot doit être arrêté proprement avec Ctrl+C
- Consultez les limites de rate limiting de l'API Telegram

## 🐛 Dépannage

### Erreurs courantes

1. **ModuleNotFoundError** :

   ```bash
   uv add install python-telegram-bot
   ou 
   pip install python-telegram-bot
   ```

2. **Token invalide** :
   Vérifiez votre token avec @BotFather

3. **Bot non répondant** :
   Vérifiez que le bot a été démarré et que l'internet fonctionne

### Support

Si vous rencontrez des problèmes, ouvrez une [issue](https://github.com/memlenz/TelegramBot/issues) sur GitHub.

Et un fichier `.gitignore` :

```gitignore
# Environments
.venv
env/
venv/
ENV/

# Python
__pycache__/
*.pyc
*.pyo
*.pyd
*.so
.Python

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Secrets
config.py
*.env
.env.local
.env.production

# Logs
*.log
logs/
```
