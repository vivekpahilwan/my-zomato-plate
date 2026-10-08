# Bakes an orders file into a single self-contained zomato-pile.html.
# Uses your real data/orders.json when present, otherwise the fictional sample.
import json, pathlib, sys

root = pathlib.Path(__file__).parent
src = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else root / "data" / "orders.json"
if not src.exists():
    src = root / "sample" / "orders.sample.json"
orders = json.loads(src.read_text())
tpl = (root / "zomato-pile.template.html").read_text()
data = json.dumps(orders, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
(root / "zomato-pile.html").write_text(tpl.replace("/*__ORDERS__*/[]", data))
print(f"wrote zomato-pile.html with {len(orders)} orders from {src}")
