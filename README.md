# my-zomato-plate

Every Zomato order I've ever placed, dumped into one pile on a single web page.

- The pile fills up in date order, left to right, oldest orders first.
- Search a dish or restaurant and every matching item flies out of the pile onto a plate, while a counter ticks up with how many you've eaten, what you spent, and a small insight ("83% from Paratha Lane. Mostly on weekdays. 16 orders, one every 17 days.").
- Search something else and the plate tips its items back onto the pile.
- Hover any item to see where it came from: restaurant, date, area, order total.


## Try it

```sh
python3 build.py sample/orders.sample.json
open zomato-pile.html
```

`sample/orders.sample.json` holds 60 made-up orders from fictional restaurants, so the page runs without anyone's real data.

## Use your own orders

The order history comes from Zomato's official MCP server (`https://mcp-server.zomato.com/mcp`), through its `get_order_history` tool.

1. On claude.ai, go to **Settings → Connectors** and add the **Zomato** connector. Sign in with your Indian mobile number. (Zomato only allows sign-ins from approved apps, and the claude.ai connector is one of them.)
2. Open Claude Code and ask it to fetch your Zomato order history into `data/orders.json` in the format below.
   - The tool returns about 20 orders per call. Passing `end_date` with the oldest date seen so far pages backwards more reliably than `postback_params`.
   - Dates come back without a year ("27 Sep"). Work the year out from the order sequence or from `start_date`/`end_date` range queries.
3. Run `python3 build.py`. When `data/orders.json` exists, the build uses it.

`data/` and the built `zomato-pile.html` are git-ignored, so your history never gets committed.

### Data format

```json
[
  {
    "id": "demo001",
    "date": "2026-09-27",
    "restaurant": "Bun Stop",
    "area": "Station Road",
    "total": 171.0,
    "status": "Delivered",
    "items": [{ "name": "Crispy Chicken Burger", "qty": 1, "addons": ["Extra Cheese"] }]
  }
]
```

## Notes

- Zomato only returns a total for each order, not per-item prices. The "spent" figure for a search splits each order's total evenly across its items.
- Emoji are chosen by keyword matching on dish names (the `EMOJI` table in `zomato-pile.template.html`). Add rules there for anything that shows up as 🍽️.
- To change the design, edit `zomato-pile.template.html`, then rebuild with `build.py`.
- The font is Montserrat. Zomato's own typeface, Okra, isn't publicly available.
- This is a personal, unofficial project and isn't affiliated with Zomato.
