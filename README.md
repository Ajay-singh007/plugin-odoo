# PayZen Odoo

PayZen Odoo is an open source payment module that links Odoo based e-commerce websites to PayZen secured payment gateway developped by Lyra Network https://www.lyra-network.com/.

For more information about PayZen, see https://payzen.eu/.

# Installation & Upgrade
- Download module archive from releases tab or in https://payzen.io/fr-FR/module-de-paiement-gratuit/#odoo.
- Unzip archive to odoo_x.y.z folder.
- If already installed, you must delete the old payment_payzen folder
- You will find already installed addons in either :
  - [ODOO_ROOT_FOLDER]/server/odoo/addons
  - /var/lib/odoo/addons/[#version]/ (Linux only)
  - `addons_path` defined in odoo.conf
- Now copy the new payment_payzen folder to Odoo addons directory
- Then you can :
  1. In your Odoo administrator interface, browse to "Configuration" tab. Here in, activate the developper mode. Then browse to "Applications" tab and click on "Update applications list".
  2. Or restart Odoo server with *sudo systemctl restart odoo* on Linux systems or by restarting Windows Odoo service. Odoo will update the applications list on startup.
- In your Odoo administrator interface, browse to "Applications" tab.
- Delete "Applications" filter from search field and search for "payzen" keyword.
- Click "Install" (or "Upgrade") button of the "PayZen Payment Acquirer" module.

# Configuration

- Go to "Website Admin" tab.
- In "Configuration" section, expand "eCommerce" menu than click on "Payment Acquirers" entry.
- Click on button "Configure" of PayZen module.
- You can now enter PayZen credentials.
