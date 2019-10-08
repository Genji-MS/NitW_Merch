# NitW_Merch
> Night in the Woods inspired artwork store (NOT for actual sale)

Mockup store to test python and mongodb interactions using HTML templates and partials

## Installing / Getting started

Requires Flask and MongoDB (pymongo). Both are application imports.
Build a test environment, Run flask, then browse the local address in your browser

```shell
Export flask_env=development; flask run
```

## Features

Displays select items from a database and simulates the shopping cart and purchase of items.
* View items from the database and add them to your cart
* Shopping cart database links items by _ID value
* Delete, items from your shopping cart
* Purchasing the same item checks for unique ID, and will increment the quantity ordered
* Purchase screen empties your cart

## Configuration

Following the database format, more items can be added, or modified. Modification of the database should only be available by the store owner.

#### Database Dictionary

Name: `title`
Type: `String`  
WhatDo: `Name of the item to be sold. Appears everywhere, also the only flavor-text detail shown in the shopping cart`

Name: `desc_sm`
Type: `String`
WhatDo: `Three word Small-Description of the individual character. Shown on the store index page`

Name: `desc_full`
Type: `String`
WhatDo: `Full-Description of the character, Only shown in the selected character page`

Name: `image_sm`
Type: `String of Image Filename`
WhatDo: `Small-Image shown in the index page and in the cart`

Name: `image_lg`
Type: `String of Image Filename`
WhatDo: `Large-Image shown in the selected characters page`

Name: `price`
Type: `float`
WhatDo: `The USD value of the item to be sold. Appears in the selected characters page, and calculated in the cart total`

## Links

Artwork is the property of xZethanyx. The Developers of Night in the Woods have requested no monetization for art in the likeness of their game. Therefore, this store is only for the sake of funsies. If you would like to request a custom commission art piece, contact the artist through their Deviant Art page. Store prices in this regard would be an accurate estimated cost.
- https://www.deviantart.com/xzethanyx

## Licensing

"The code in this project is licensed under MIT license."

The Artwork included in this repo is not licencesed for your use.