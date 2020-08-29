import argparse
import abstract_factory

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--class_name", help="class_name", required=True)
    args = parser.parse_args()
    fac = abstract_factory.Factory.get_factory(classname=args.class_name)

    asahi = fac.create_link('朝日新聞', 'http://...')
    yomiuri = fac.create_link('読売新聞', 'http://...')

    us_yahoo = fac.create_link('Yahoo!', 'http://...')
    jp_yahoo = fac.create_link('Yahoo!Japan', 'http://...')
    exite = fac.create_link('Excite', 'http://...')
    google = fac.create_link('Google', 'http://...')

    traynews = fac.create_tray('新聞')
    traynews.add(asahi)
    traynews.add(yomiuri)

    trayyahoo = fac.create_tray('Yahoo!')
    trayyahoo.add(us_yahoo)
    trayyahoo.add(jp_yahoo)

    traysearch = fac.create_tray('サーチエンジン')
    traysearch.add(trayyahoo)
    traysearch.add(exite)
    traysearch.add(google)

    page = fac.create_page('LinkPage', '結城　浩')
    page.add(traynews)
    page.add(traysearch)
    page.output()
