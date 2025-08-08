import { useEffect } from "react";

export function useSEO({ title, description, canonical }: { title: string; description: string; canonical?: string }){
  useEffect(() => {
    document.title = title;
    const setMeta = (name: string, content: string) => {
      let tag = document.querySelector(`meta[name="${name}"]`) as HTMLMetaElement | null;
      if (!tag){ tag = document.createElement('meta'); tag.setAttribute('name', name); document.head.appendChild(tag); }
      tag.setAttribute('content', content);
    };
    setMeta('description', description);
    const ogTitle = document.querySelector('meta[property="og:title"]') || document.createElement('meta');
    ogTitle.setAttribute('property','og:title'); ogTitle.setAttribute('content', title); if(!ogTitle.parentElement) document.head.appendChild(ogTitle);
    const ogDesc = document.querySelector('meta[property="og:description"]') || document.createElement('meta');
    ogDesc.setAttribute('property','og:description'); ogDesc.setAttribute('content', description); if(!ogDesc.parentElement) document.head.appendChild(ogDesc);
    if (canonical){
      let link = document.querySelector('link[rel="canonical"]') as HTMLLinkElement | null;
      if (!link){ link = document.createElement('link'); link.setAttribute('rel','canonical'); document.head.appendChild(link); }
      link.setAttribute('href', canonical);
    }
  }, [title, description, canonical]);
}
