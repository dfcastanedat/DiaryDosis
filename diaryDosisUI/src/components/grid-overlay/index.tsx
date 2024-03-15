import { KeyboardEvent, useState, useEffect } from "react"

/**
 * A component that displays a debug overlay for the grid system.
 */
export default function index(): JSX.Element {
    const [showOverlay, setShowOverlay] = useState(false);
    useEffect(() => {
      window.document.addEventListener('keydown', onKeyDown);
    
      return () => {
        window.document.removeEventListener('keydown', onKeyDown)
      }
    }, []);

    /**
     * A function that handles keydown events, toggling overlay when 'Shift + G' is pressed.
     * @param {Event} e - the keydown event
     */
    const onKeyDown = (e: Event) => {
        let event = e as unknown as KeyboardEvent
        if(event.key === 'G' && event.shiftKey) {
            setShowOverlay((prevState) => !prevState);
        }
    }

    return (
        <>
        {showOverlay && 
            <div className="grid-overlay">
                {Array.from({ length: 12 }).map((_, index) => (
                    <div className="grid-overlay__column" key={index}>{index}</div>
                ))}
            </div>
        }
        </>
    )
}
