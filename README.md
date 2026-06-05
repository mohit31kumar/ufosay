# ufosay

A flying saucer terminal animation tool — like `sl` meets `cowsay`.

```
 ┌──────────────────────────────┐
 │ We will conquer the earth!!  │
 └──────────────────────────────┘
        _.---._
      .'       '.
  _.-~===========~-._
 (___O___O___O___O___)    ← blinking windows
       \_______/
        ·|·               ← pulsing tractor beam
       ·/|\·
      ·/ | \·
~~~~~~~~~~~~~~~~~~~~~~~~~~  ← fixed terrain
```

- Flies **right to left** at 60fps (butter smooth)
- **Pauses mid-screen** to let you read the message
- Shows a **cowsay-style speech bubble**
- **Blinking windows**, **pulsing tractor beam**, **floating motion**, **stars**, **terrain**

## Install

### Via pip (recommended)

```bash
pip install ufosay
```

### From source

```bash
git clone https://github.com/YOUR_USERNAME/ufosay.git
cd ufosay
pip install .
```

## Usage

```bash
ufosay                          # UFO flies by silently
ufosay "Hello from space!"      # UFO with speech bubble
echo "hi" | ufosay              # Pipe input like cowsay
ufosay --msg "text"             # Explicit message flag
ufosay --help                   # Show usage
```

### Examples

```bash
ufosay "We will conquer the earth!!"
```

```
 ________________________________________
/ We will conquer                        \
| the earth!!                            |
\                                        /
 ----------------------------------------
        _.---._
      .'       '.
  _.-~===========~-._
 (___________________)
       \_______/
```

## Animation details

| Feature | Detail |
|---------|--------|
| Frame rate | 60 fps |
| Movement | 30 cols/sec (1 col per 2 frames) |
| Direction | Right to left |
| Mid-screen pause | 0.5 seconds per word |
| Vertical float | Frozen during pause for readability |
| Window blink | Alternates every ~0.33s |
| Tractor beam | Pulses every ~0.27s |
| Bubble style | Cowsay-style, word-wrapped at 40 chars |
| Bubble visibility | Only during mid-screen pause |
| Terrain | Fixed `~` row at bottom |
| Clean exit | Ctrl+C restores cursor, no leftover text |

## Mistype triggers (optional)

If you frequently mistype `ls`, run one of the install scripts to set up automatic triggers:

### Linux / macOS

```bash
./install.sh
```

This adds aliases to `~/.bashrc` or `~/.zshrc`:

| Typo | Triggers |
|------|----------|
| `ks` | `ufosay "Did you mean ls?"` |
| `cl` | `ufosay "Did you mean ls?"` |
| `xl` | `ufosay "Did you mean ls?"` |
| `lw` | `ufosay "Did you mean ls?"` |
| `lz` | `ufosay "Did you mean ls?"` |

### Windows PowerShell

```powershell
.\install.ps1
```

### Windows CMD

```cmd
install.bat
```

## Requirements

- Python 3.8 or later
- Any terminal that supports ANSI escape codes (all modern terminals do)

## License

MIT
