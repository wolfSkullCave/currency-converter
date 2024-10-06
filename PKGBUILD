pkgname=currency-converter
pkgver=0.0.1
pkgrel=1
pkgdesc="Converts dollars to rands"
arch=('any')
url="https://example.com/my-python-app"
license=('MIT')
depends=('python')
source=("https://github.com/wolfSkullCave/currency-converter/tree/aur-package")
sha256sums=('SKIP')  # Replace with actual checksum if available

build() {
    cd "$srcdir/$pkgname-$pkgver"
    python setup.py build
}

package() {
    cd "$srcdir/$pkgname-$pkgver"
    python setup.py install --root="$pkgdir"
}
