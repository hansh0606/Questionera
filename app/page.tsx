import Link from "next/link";
import { Stats } from "./components/stats";
import { Testimonials } from "./components/testimony";

export default function Home() {
  return (
    <div className="flex flex-col gap-8 pb-8 md:gap-16 md:pb-16 xl:pb-24">
      <div className="flex flex-col items-center justify-center max-w-3xl px-8 mx-auto mt-8 sm:min-h-screen sm:mt-0 sm:px-0">
        <div className="hidden sm:mb-8 sm:flex sm:justify-center">
          {/* <Link
            href="https://github.com/chronark/envshare"
            className="text-zinc-400 relative overflow-hidden rounded-full py-1.5 px-4 text-sm leading-6 ring-1 ring-zinc-100/10 hover:ring-zinc-100/30 duration-150"
          >
            EnvShare is Open Source on{" "}
            <span className="font-semibold text-zinc-200">
              GitHub <span aria-hidden="true">&rarr;</span>
            </span>
          </Link> */}
        </div>
        <div>
          <h2 className="py-4 text-2xl font-bold tracking-tight text-center text-transparent bg-gradient-to-t bg-clip-text from-zinc-100/50 to-white sm:text-5xl">
          Your one Stop Solution for all Interview Revision 
          </h2>
          <p className="mt-6 leading-5 text-zinc-600 sm:text-center">
          Your privacy matters to us. Your resume is encrypted in your browser before being briefly stored for generating interview questions. Rest assured, your data never leaves your browser unencrypted. Your trust is our priority.
          </p>
          <div className="flex flex-col justify-center gap-4 mx-auto mt-8 sm:flex-row sm:max-w-lg ">
            
            <Link
              href="/share"
              className="sm:w-1/2 sm:text-center inline-block transition-all space-x-2  rounded px-4 py-1.5 md:py-2 text-base font-semibold leading-7 text-zinc-800   bg-zinc-50 ring-1 ring-transparent hover:text-zinc-100 hover:ring-zinc-600/80  hover:bg-zinc-900/20 duration-150 hover:drop-shadow-cta"
            >
              <span>Share</span>
              <span aria-hidden="true">&rarr;</span>
            </Link>
          </div>
        </div>
      </div>
      <h2 className="py-4 text-3xl font-bold text-center text-zinc-300 ">Used and trusted by a growing community</h2>
      <Stats />
      {/* <Testimonials /> */}
    </div>
  );
}
