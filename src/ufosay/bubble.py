def word_wrap(text, max_width):
    words = text.split()
    lines = []
    cur = []
    cur_len = 0
    for w in words:
        wlen = len(w)
        if cur_len + wlen + len(cur) > max_width:
            lines.append(" ".join(cur))
            cur = [w]
            cur_len = wlen
        else:
            cur.append(w)
            cur_len += wlen
    if cur:
        lines.append(" ".join(cur))
    return lines if lines else [""]


def make_bubble(text, max_width=40):
    if not text:
        return []
    lines = word_wrap(text, max_width)
    cw = max(len(l) for l in lines)
    pw = cw + 2
    out = []
    out.append(" " + "_" * pw)
    if len(lines) == 1:
        out.append("< " + lines[0].ljust(cw) + " >")
    else:
        for i, l in enumerate(lines):
            if i == 0:
                out.append("/ " + l.ljust(cw) + " \\")
            elif i == len(lines) - 1:
                out.append("\\ " + l.ljust(cw) + " /")
            else:
                out.append("| " + l.ljust(cw) + " |")
    out.append(" " + "-" * pw)
    return out
